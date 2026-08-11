/* ==========================================================================
   AgriBridge AI - Vanilla JavaScript Interactivity
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // Sync localStorage language preference on load if set
    const savedLang = localStorage.getItem('agri_lang');
    const langSelect = document.getElementById('langSelect');
    
    if (savedLang && langSelect && langSelect.value !== savedLang) {
        // Option to sync if needed
    }

    // Format any initial or server-rendered chat bubble text
    document.querySelectorAll('.bubble-text').forEach(el => {
        if (!el.dataset.formatted) {
            el.innerHTML = formatMarkdownToHTML(el.innerText || el.textContent);
            el.dataset.formatted = 'true';
        }
    });

    // Scroll chat to bottom if chat container exists
    scrollChatToBottom();
});

/**
 * Parse markdown string responses dynamically into safe HTML.
 * Supports: headings, bold, italic, bullet lists, numbered lists,
 *           inline code, fenced code blocks, paragraphs.
 * All user/AI text is HTML-escaped before parsing to prevent injection.
 */
function formatMarkdownToHTML(text) {
    if (!text) return '';

    // --- Step 1: Extract and protect fenced code blocks (``` ... ```) ---
    const codeBlocks = [];
    text = text.replace(/```[\s\S]*?```/g, function(match) {
        const inner = match.replace(/^```[^\n]*\n?/, '').replace(/```$/, '');
        const escaped = inner
            .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        codeBlocks.push('<pre><code>' + escaped + '</code></pre>');
        return '\x00CODEBLOCK' + (codeBlocks.length - 1) + '\x00';
    });

    // --- Step 2: Process line-by-line ---
    const lines = text.split('\n');
    let result = '';
    let inList = false;
    let inOList = false;

    lines.forEach(function(rawLine) {
        // Restore code blocks that may appear as their own line placeholder
        if (/^\x00CODEBLOCK\d+\x00$/.test(rawLine.trim())) {
            if (inList)  { result += '</ul>';  inList  = false; }
            if (inOList) { result += '</ol>';  inOList = false; }
            const idx = parseInt(rawLine.trim().replace(/\x00CODEBLOCK(\d+)\x00/, '$1'), 10);
            result += codeBlocks[idx];
            return;
        }

        // HTML-escape this line's text content
        let line = rawLine
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');

        const trimmed = line.trim();

        // --- Headings: ### H3  ## H2  # H1 ---
        const hMatch = trimmed.match(/^(#{1,3})\s+(.+)$/);
        if (hMatch) {
            if (inList)  { result += '</ul>';  inList  = false; }
            if (inOList) { result += '</ol>';  inOList = false; }
            const level = hMatch[1].length + 2; // h3/h4/h5 — keeps visual hierarchy modest
            const headingLevel = Math.min(level, 6);
            result += `<h${headingLevel} class="bubble-heading">${applyInline(hMatch[2])}</h${headingLevel}>`;
            return;
        }

        // --- Numbered lists: "1. " / "2. " etc ---
        const olMatch = trimmed.match(/^(\d+)\.\s+(.+)$/);
        if (olMatch) {
            if (inList) { result += '</ul>'; inList = false; }
            if (!inOList) { result += '<ol class="chat-list">'; inOList = true; }
            result += `<li>${applyInline(olMatch[2])}</li>`;
            return;
        }

        // --- Bullet lists: "• " / "- " / "* " ---
        if (trimmed.startsWith('•') || trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
            if (inOList) { result += '</ol>'; inOList = false; }
            if (!inList) { result += '<ul class="chat-list">'; inList = true; }
            const item = trimmed.replace(/^[•\-\*]\s*/, '');
            result += `<li>${applyInline(item)}</li>`;
            return;
        }

        // Close any open list before normal paragraph
        if (inList)  { result += '</ul>';  inList  = false; }
        if (inOList) { result += '</ol>';  inOList = false; }

        if (trimmed.length > 0) {
            result += `<p>${applyInline(trimmed)}</p>`;
        }
    });

    if (inList)  result += '</ul>';
    if (inOList) result += '</ol>';

    // Restore any remaining code block placeholders (edge case: inline in paragraphs already handled)
    result = result.replace(/\x00CODEBLOCK(\d+)\x00/g, function(_, idx) {
        return codeBlocks[parseInt(idx, 10)];
    });

    return result || text;
}

/**
 * Apply inline markdown (bold, italic, inline code) to an already HTML-escaped string.
 * Called on individual lines/items after outer escaping is done.
 */
function applyInline(str) {
    // Inline code: `code` (must come before bold/italic to avoid mis-parsing backtick content)
    str = str.replace(/`([^`]+)`/g, '<code>$1</code>');
    // Bold: **text** or __text__
    str = str.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    str = str.replace(/__(.*?)__/g, '<strong>$1</strong>');
    // Italic: *text* (only when not part of **)
    str = str.replace(/(?<!\*)\*([^\*\n]+)\*(?!\*)/g, '<em>$1</em>');
    return str;
}

/**
 * Switch application language asynchronously via POST /set-language
 */
function changeLanguage(lang) {
    if (!lang) return;

    fetch('/set-language', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({ lang: lang })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            localStorage.setItem('agri_lang', lang);
            // Reload page to reflect full translated template render
            window.location.reload();
        } else {
            console.error('Language switch error:', data.message);
        }
    })
    .catch(err => {
        console.error('Error connecting to language API:', err);
    });
}

/**
 * Handle form submit loading indicators and double-submit prevention
 */
function submitFormWithLoading(formElement) {
    const submitBtn = formElement.querySelector('.btn-submit');
    if (!submitBtn) return;

    const btnText = submitBtn.querySelector('.btn-text');
    const btnSpinner = submitBtn.querySelector('.btn-spinner');

    // Disable button to prevent rapid double-clicks
    submitBtn.disabled = true;

    if (btnText && btnSpinner) {
        btnText.style.opacity = '0.5';
        btnSpinner.classList.remove('hidden');
    }
}

/**
 * Preview crop image before uploading & validate client-side size (2MB)
 */
function previewCropImage(input) {
    const uploadText = document.getElementById('uploadText');
    const previewContainer = document.getElementById('imagePreviewContainer');
    const previewImg = document.getElementById('imagePreview');

    if (input.files && input.files[0]) {
        const file = input.files[0];
        
        // 2MB size check (2 * 1024 * 1024 bytes)
        if (file.size > 2 * 1024 * 1024) {
            alert('File size exceeds the 2MB limit! Please select a smaller photo.');
            input.value = '';
            if (previewContainer) previewContainer.classList.add('hidden');
            if (uploadText) uploadText.innerText = 'Tap to select or take leaf photo (JPG/PNG)';
            return;
        }

        const reader = new FileReader();
        reader.onload = function(e) {
            if (previewImg) previewImg.src = e.target.result;
            if (previewContainer) previewContainer.classList.remove('hidden');
            if (uploadText) uploadText.innerText = 'Selected: ' + file.name;
        };
        reader.readAsDataURL(file);
    }
}

/**
 * Quick prompt filler for chatbot chips
 */
function sendQuickPrompt(promptText) {
    const chatInput = document.getElementById('chatInput');
    if (chatInput) {
        chatInput.value = promptText;
        chatInput.focus();
        submitChatMessage();
    }
}

/**
 * Asynchronous chat message submission
 */
function submitChatMessage(event) {
    if (event && event.preventDefault) {
        event.preventDefault();
    }
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');
    const submitBtn = document.getElementById('chatSubmitBtn');

    if (!chatInput || !chatInput.value.trim()) return;

    const userMessage = chatInput.value.trim();
    chatInput.value = '';

    // Append User Bubble
    appendBubble(chatMessages, '👨‍🌾 You', userMessage, 'user-bubble');
    scrollChatToBottom();

    // Disable button temporarily
    if (submitBtn) submitBtn.disabled = true;

    // Send POST request to /chat
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(res => res.json())
    .then(data => {
        if (data.response) {
            appendBubble(chatMessages, '🤖 AgriBridge Assistant', data.response, 'bot-bubble');
            scrollChatToBottom();
        }
    })
    .catch(err => {
        console.error('Chat error:', err);
        appendBubble(chatMessages, '🤖 AgriBridge Assistant', 'Connection error. Please try again.', 'bot-bubble');
    })
    .finally(() => {
        if (submitBtn) submitBtn.disabled = false;
        chatInput.focus();
    });
}

function appendBubble(container, senderName, textContent, bubbleClass) {
    if (!container) return;
    const bubbleDiv = document.createElement('div');
    bubbleDiv.className = 'chat-bubble ' + bubbleClass;
    
    const senderDiv = document.createElement('div');
    senderDiv.className = 'bubble-sender';
    senderDiv.innerText = senderName;
    
    const textDiv = document.createElement('div');
    textDiv.className = 'bubble-text';
    textDiv.dataset.formatted = 'true';
    textDiv.innerHTML = formatMarkdownToHTML(textContent);

    bubbleDiv.appendChild(senderDiv);
    bubbleDiv.appendChild(textDiv);
    container.appendChild(bubbleDiv);
}

function scrollChatToBottom() {
    const chatMessages = document.getElementById('chatMessages');
    if (chatMessages) {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}

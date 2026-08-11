import os
import time
from flask import Flask, render_template, request, session, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
from markupsafe import escape

from config import Config
from translations import get_translation, TRANSLATIONS
from modules.weather import get_weather_advisory
from modules.soil import get_soil_guidance
from modules.crop import allowed_file, validate_image_file, analyze_crop_disease
from modules.chat import process_chat_message

app = Flask(__name__)
app.config.from_object(Config)

# Automatically create uploads directory if it does not exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.before_request
def ensure_language():
    """Ensure session contains a valid language default."""
    if 'lang' not in session or session['lang'] not in Config.SUPPORTED_LANGUAGES:
        session['lang'] = Config.DEFAULT_LANGUAGE

def current_lang():
    return session.get('lang', Config.DEFAULT_LANGUAGE)

def t(key, default=None):
    return get_translation(current_lang(), key, default)

@app.context_processor
def inject_globals():
    """Inject translation helper and global variables into all templates."""
    return {
        't': t,
        'current_lang': current_lang(),
        'supported_languages': Config.SUPPORTED_LANGUAGES
    }

# ----------------------------------------------------
# Routes
# ----------------------------------------------------

@app.route('/')
def index():
    """Home page with feature cards and branding."""
    return render_template('index.html')

@app.route('/set-language', methods=['POST'])
def set_language():
    """Sets current user language in session and returns JSON response."""
    data = request.get_json(silent=True) or request.form
    lang = data.get('lang', '').strip().lower()
    
    if lang in Config.SUPPORTED_LANGUAGES:
        session['lang'] = lang
        return jsonify({
            'status': 'success',
            'lang': lang,
            'message': f"Language changed to {lang}"
        })
    return jsonify({
        'status': 'error',
        'message': 'Unsupported language'
    }), 400

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    """Weather module route."""
    if request.method == 'POST':
        city = escape(request.form.get('city', '').strip())
        if not city:
            flash(t('err_invalid_city'), 'error')
            return render_template('weather.html', result=None)
        
        result = get_weather_advisory(city, lang=current_lang())
        return render_template('weather.html', result=result, city_input=city)
        
    return render_template('weather.html', result=None)

@app.route('/soil', methods=['GET', 'POST'])
def soil():
    """Soil guidance module route."""
    if request.method == 'POST':
        moisture = escape(request.form.get('moisture', 'moist'))
        crop_name = escape(request.form.get('crop_name', '').strip())
        growth_stage = escape(request.form.get('growth_stage', 'vegetative'))
        soil_type = escape(request.form.get('soil_type', 'any'))

        if not crop_name:
            crop_name = "Crop"

        guidance = get_soil_guidance(moisture, crop_name, growth_stage, soil_type, lang=current_lang())
        return render_template('soil.html', result=guidance)

    return render_template('soil.html', result=None)

@app.route('/crop', methods=['GET', 'POST'])
def crop():
    """Crop disease detection module route."""
    if request.method == 'POST':
        if 'crop_image' not in request.files:
            flash(t('err_no_file'), 'error')
            return render_template('crop.html', result=None)

        file = request.files['crop_image']
        if file.filename == '':
            flash(t('err_no_file'), 'error')
            return render_template('crop.html', result=None)

        if file and allowed_file(file.filename):
            safe_fn = secure_filename(file.filename)
            timestamp = int(time.time())
            saved_filename = f"crop_{timestamp}_{safe_fn}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], saved_filename)
            file.save(file_path)

            # Validate image format using Pillow and check size
            is_valid, err_msg = validate_image_file(file_path)
            if not is_valid:
                # Remove invalid file
                if os.path.exists(file_path):
                    os.remove(file_path)
                flash(err_msg, 'error')
                return render_template('crop.html', result=None)

            analysis = analyze_crop_disease(saved_filename, lang=current_lang())
            analysis['file_url'] = url_for('uploaded_file', filename=saved_filename)
            return render_template('crop.html', result=analysis)
        else:
            flash(t('err_invalid_file'), 'error')
            return render_template('crop.html', result=None)

    return render_template('crop.html', result=None)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded crop files securely."""
    from flask import send_from_directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], secure_filename(filename))

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """Interactive offline farming chatbot route."""
    if request.method == 'POST':
        # Accept JSON or form payload
        if request.is_json:
            data = request.get_json()
            user_msg = escape(data.get('message', '').strip())
            reply = process_chat_message(user_msg, lang=current_lang())
            return jsonify({'response': reply})
        else:
            user_msg = escape(request.form.get('message', '').strip())
            reply = process_chat_message(user_msg, lang=current_lang())
            return render_template('chat.html', last_message=user_msg, last_reply=reply)

    return render_template('chat.html')

@app.route('/result')
def result():
    """Generic formatted result page view."""
    feature = escape(request.args.get('feature', 'General Advisory'))
    problem = escape(request.args.get('problem', 'Field Check'))
    reason = escape(request.args.get('reason', 'Weather or Soil conditions'))
    solution = escape(request.args.get('solution', 'Follow good agronomic practices.'))
    tip = escape(request.args.get('tip', 'Regular field monitoring.'))
    is_demo = request.args.get('demo', 'true').lower() == 'true'

    return render_template('result.html',
                           feature=feature,
                           problem=problem,
                           reason=reason,
                           solution=solution,
                           tip=tip,
                           is_demo=is_demo)

@app.route('/health')
def health():
    """Health check JSON route confirming server status."""
    return jsonify({
        'status': 'ok',
        'app': 'AgriBridge AI',
        'version': '1.0.0',
        'environment': 'development',
        'weather_provider': 'Open-Meteo (no API key required)'
    })

# ----------------------------------------------------
# Error Handlers
# ----------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

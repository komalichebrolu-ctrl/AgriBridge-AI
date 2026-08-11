import os
import random
from werkzeug.utils import secure_filename
from PIL import Image
from translations import get_translation

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_image_file(file_path):
    """Checks if file is a valid readable image using Pillow and <= 2MB size."""
    try:
        if not os.path.exists(file_path):
            return False, "File does not exist."
        
        size = os.path.getsize(file_path)
        if size > 2 * 1024 * 1024:
            return False, "File size exceeds 2MB limit."
        
        with Image.open(file_path) as img:
            img.verify()
        return True, "Valid Image"
    except Exception as e:
        return False, "Invalid image format or corrupted file."

def analyze_crop_disease(filename, lang='en'):
    """
    Simulates disease detection on uploaded crop photo.
    Returns simulated condition, confidence, cause, treatment, prevention tip, and disclaimer.
    """
    # Deterministic simulation based on filename hash to give consistent output for same image
    fn_hash = sum(ord(c) for c in filename)
    conditions = ['healthy', 'leaf_spot', 'powdery_mildew', 'nutrient_stress']
    chosen_condition = conditions[fn_hash % len(conditions)]
    
    # Confidence score simulation (85% to 96%)
    random.seed(fn_hash)
    confidence_score = random.randint(86, 95)
    random.seed()

    if chosen_condition == 'healthy':
        if lang == 'hi':
            condition_str = "स्वस्थ फसल (कोई बीमारी नहीं)"
            cause_str = "फसल में पर्याप्त पोषण और अनुकूल मौसम की स्थिति पाई गई।"
            treatment_str = "किसी रासायनिक या जैविक उपचार की आवश्यकता नहीं है। वर्तमान देखभाल जारी रखें।"
            prevention_str = "नियमित रूप से खेत का निरीक्षण करें और संतुलित सिंचाई बनाए रखें।"
        elif lang == 'te':
            condition_str = "ఆరోగ్యకరమైన పంట (తెగుళ్ళు లేవు)"
            cause_str = "పంటకు సరిపడా పోషకాలు మరియు అనుకూలమైన వాతావరణం ఉంది."
            treatment_str = "ఎటువంటి మందులు చల్లాల్సిన అవసరం లేదు. ప్రస్తుతం చేస్తున్న సంరక్షణ కొనసాగించండి."
            prevention_str = "పొలాన్ని క్రమం తప్పకుండా పరిశీలిస్తూ, తగినంత నీటి తడి అందించండి."
        else:
            condition_str = "Healthy Crop (No Disease Detected)"
            cause_str = "Good plant vigor, optimal nutrition, and clean foliage observed."
            treatment_str = "No chemical or biological spray required. Maintain current farming practices."
            prevention_str = "Continue regular monitoring and practice balanced crop irrigation."

    elif chosen_condition == 'leaf_spot':
        if lang == 'hi':
            condition_str = "पत्ती का धब्बा रोग (Leaf Spot / Fungal Infection)"
            cause_str = "अधिक नमी या पत्तों पर पानी जमा रहने के कारण फफूंद संक्रमण।"
            treatment_str = "संक्रमित पत्तियों को निकालकर नष्ट करें। नीम के तेल (5ml/लीटर) या अनुशंसित जैविक फफूंदनाशी का छिड़काव करें।"
            prevention_str = "पौधों के बीच पर्याप्त दूरी रखें ताकि हवा और धूप पत्तियों तक पहुंच सके।"
        elif lang == 'te':
            condition_str = "ఆకు మచ్చ తెగులు (Leaf Spot / ఫంగస్ ఇన్ఫెక్షన్)"
            cause_str = "అధిక తేమ లేదా ఆకులపై నీరు నిలిచి ఉండటం వల్ల శిలీంధ్రం (ఫంగస్) వ్యాపించింది."
            treatment_str = "తెగులు సోకిన ఆకులను తీసివేసి నాశనం చేయండి. వేపనూనె (లీటరుకు 5ml) పిచికారీ చేయండి."
            prevention_str = "గాలి, ఎండ సరిగ్గా తగిలేలా మొక్కల మధ్య తగినంత దూరం పాటించండి."
        else:
            condition_str = "Leaf Spot Disease (Fungal Infection)"
            cause_str = "High ambient humidity and leaf wetness promoting fungal spore growth."
            treatment_str = "Remove heavily infected leaves. Apply Neem oil solution (5ml/L water) or bio-fungicide."
            prevention_str = "Ensure adequate spacing between plants for ventilation and avoid overhead irrigation."

    elif chosen_condition == 'powdery_mildew':
        if lang == 'hi':
            condition_str = "पाउडरी मिल्ड्यू (सफेद चूर्ण रोग)"
            cause_str = "सूखे मौसम में रात की नमी और हवा के माध्यम से फफूंद के बीजाणुओं का फैलना।"
            treatment_str = "प्रभावित भागों पर 0.3% घुलनशील गंधक (सल्फर) या खट्टी छाछ का पानी मिलाकर छिड़काव करें।"
            prevention_str = "खेत को खरपतवार मुक्त रखें और अत्यधिक नाइट्रोजन खाद के प्रयोग से बचें।"
        elif lang == 'te':
            condition_str = "బూడిద తెగులు (Powdery Mildew)"
            cause_str = "పొడి వాతావరణంలో రాత్రి వేళ ఉండే తేమ వల్ల బూడిద వంటి శిలీంధ్రం వ్యాపిస్తుంది."
            treatment_str = "కరిగే సల్ఫర్ (గంధకం) లేదా పులిసిన మజ్జిగ నీటిని ఆకులపై పిచికారీ చేయండి."
            prevention_str = "పొలంలో కలుపు లేకుండా చూసుకోండి మరియు అధిక మోతాదులో నత్రజని ఎరువులు వేయకండి."
        else:
            condition_str = "Powdery Mildew (White Powder Fungus)"
            cause_str = "Fungal infection thriving in dry daytime weather with high nighttime air humidity."
            treatment_str = "Spray wettable sulfur (0.3%) or fermented buttermilk solution on affected leaves."
            prevention_str = "Keep field weed-free and avoid excessive nitrogenous fertilizing."

    else: # nutrient_stress
        if lang == 'hi':
            condition_str = "पोषक तत्वों की कमी (Nutrient Stress / Yellowing)"
            cause_str = "मिट्टी में नाइट्रोजन या लोहे (Iron/Zinc) की कमी या जड़ों द्वारा पोषण न ले पाना।"
            treatment_str = "अच्छी तरह सड़ी हुई गोबर की खाद (FYM) और सूक्ष्म पोषक मिश्रण (Micronutrient Spray) का प्रयोग करें।"
            prevention_str = "बुआई से पहले मिट्टी परीक्षण करवाएं और संतुलित खाद प्रबंधन अपनाएं।"
        elif lang == 'te':
            condition_str = "పోషకాల లోపం (Nutrient Deficiency / పసుపు రంగు మారడం)"
            cause_str = "నేలలో నత్రజని లేదా ఇనుము/జింక్ లోపం ఉండటం లేదా వేర్లు పోషకాలను తీసుకోలేకపోవడం."
            treatment_str = "బాగా దక్కిన పశువుల ఎరువు మరియు మైక్రోన్యూట్రియెంట్ పిచికారీ చేయండి."
            prevention_str = "విత్తే ముందు నేల పరీక్ష చేయించి, సమగ్ర పోషక యాజమాన్యం పాటించండి."
        else:
            condition_str = "Nutrient Stress / Chlorosis (Yellowing Leaves)"
            cause_str = "Nitrogen or micronutrient (Iron/Zinc) deficiency or root uptake restriction."
            treatment_str = "Apply well-decomposed organic farmyard manure and foliar micronutrient spray."
            prevention_str = "Conduct soil testing prior to planting and maintain balanced fertilizing."

    disclaimer = get_translation(lang, 'crop_disclaimer')

    return {
        'filename': filename,
        'condition': condition_str,
        'confidence': f"{confidence_score}% (Simulated)",
        'cause': cause_str,
        'treatment': treatment_str,
        'prevention': prevention_str,
        'disclaimer': disclaimer,
        'is_demo': True,
        'badge_text': get_translation(lang, 'demo_mode_badge')
    }

from translations import get_translation

def get_soil_guidance(moisture, crop_name, growth_stage, soil_type='any', lang='en'):
    """
    Generates irrigation and general fertilizer guidance based on soil moisture, crop stage, and soil type.
    """
    crop = crop_name.strip() if crop_name else "Crop"
    moisture = moisture.lower() if moisture else "moist"
    growth_stage = growth_stage.lower() if growth_stage else "vegetative"
    soil_type = soil_type.lower() if soil_type else "any"

    # 1. Irrigation Advice Logic
    irrigation_advice = ""
    if moisture == "dry":
        if growth_stage in ["flowering", "fruiting"]:
            if lang == 'hi':
                irrigation_advice = f"{crop} की {growth_stage} अवस्था में मिट्टी सूखी है। तुरंत हल्की सिंचाई करें क्योंकि पानी की कमी से फूल और फल गिर सकते हैं।"
            elif lang == 'te':
                irrigation_advice = f"{crop} పంట {growth_stage} దశలో నేల పొడిగా ఉంది. పూత మరియు కాయ రాలకుండా తక్షణమే తేలికపాటి నీటి తడి అందించండి."
            else:
                irrigation_advice = f"The soil is dry during critical {growth_stage} stage for {crop}. Apply immediate light irrigation to prevent flower/fruit drop."
        else:
            if lang == 'hi':
                irrigation_advice = f"मिट्टी में नमी कम है। {crop} के स्वस्थ विकास के लिए पर्याप्त सिंचाई करें।"
            elif lang == 'te':
                irrigation_advice = f"నేలలో తేమ తక్కువగా ఉంది. {crop} పంట సక్రమంగా పెరగడానికి తగినంత నీటి తడి ఇవ్వండి."
            else:
                irrigation_advice = f"Soil moisture is low. Irrigation is recommended for uniform growth of {crop}."
    elif moisture == "wet":
        if lang == 'hi':
            irrigation_advice = f"खेत में अत्यधिक नमी या पानी भरा हुआ है। सिंचाई तुरंत रोकें और अतिरिक्त पानी की निकासी (ड्रेनेज) की व्यवस्था करें।"
        elif lang == 'te':
            irrigation_advice = f"పొలంలో నీరు ఎక్కువగా ఉంది లేదా నీరు నిలిచి ఉంది. నీటి తడిని వెంటనే నిలిపివేసి, నీరు బయటకు పోయేలా కాలువలు తీయండి."
        else:
            irrigation_advice = f"The soil is saturated or waterlogged. Stop irrigation immediately and ensure proper field drainage."
    else: # moist
        if lang == 'hi':
            irrigation_advice = f"मिट्टी में नमी का स्तर {crop} के लिए अनुकूल है। अभी सिंचाई की आवश्यकता नहीं है। 2-3 दिन बाद पुनः जांच करें।"
        elif lang == 'te':
            irrigation_advice = f"నేలలో తేమ శాతము {crop} పంటకు అనుకూలంగా ఉంది. ప్రస్తుతం నీటి తడి అవసరం లేదు. 2-3 రోజుల తర్వాత పరిశీలించండి."
        else:
            irrigation_advice = f"Soil moisture is at an optimal level for {crop}. No immediate irrigation needed. Re-check in 2–3 days."

    # 2. General Fertilizer Guidance Logic
    fertilizer_advice = ""
    if growth_stage == "seedling":
        if lang == 'hi':
            fertilizer_advice = f"शुरुआती (अंकुरण) अवस्था: जड़ों के विकास के लिए फास्फोरस (P) युक्त जैविक खाद या कम्पोस्ट का प्रयोग करें।"
        elif lang == 'te':
            fertilizer_advice = f"ప్రారంభ (మొలక) దశ: వేర్ల అభివృద్ధికి భాస్వరం (P) కలిగిన ససేమిరా ఎరువులు లేదా పశువుల ఎరువు వాడండి."
        else:
            fertilizer_advice = f"Early Seedling Stage: Focus on root development using balanced organic manure or phosphorus-rich basal application."
    elif growth_stage == "vegetative":
        if lang == 'hi':
            fertilizer_advice = f"वानस्पतिक अवस्था: पत्तियों और तने की बढ़वार के लिए नाइट्रोजन (N) की आवश्यकता होती है। पर्याप्त नमी में ही खाद डालें।"
        elif lang == 'te':
            fertilizer_advice = f"శాకీయ పెరుగుదల దశ: ఆకులు, కొమ్మల పెరిగేందుకు నత్రజని (N) అవసరం. నేలలో తేమ ఉన్నప్పుడే ఎరువులు వేయాలి."
        else:
            fertilizer_advice = f"Vegetative Stage: Vegetative shoot growth benefits from split nitrogen applications when soil moisture is adequate."
    elif growth_stage == "flowering":
        if moisture == "dry":
            if lang == 'hi':
                fertilizer_advice = f"फूल आने की अवस्था: मिट्टी सूखी होने पर रासायनिक खाद न डालें। पहले सिंचाई करें, फिर पोटैशियम (K) एवं सूक्ष्म पोषक तत्व दें।"
            elif lang == 'te':
                fertilizer_advice = f"పూత దశ: నేల పొడిగా ఉన్నప్పుడు ఎరువులు వేయకండి. తడి ఇచ్చిన తర్వాత పొటాషియం (K) మరియు సూక్ష్మ పోషకాలు అందించండి."
            else:
                fertilizer_advice = f"Flowering Stage: Do not apply heavy fertilizers under moisture stress. Irrigate first, then supply potassium (K) and micronutrients."
        else:
            if lang == 'hi':
                fertilizer_advice = f"फूल आने की अवस्था: फूलों के बेहतर विकास के लिए पोटैशियम और बोरोन जैसे सूक्ष्म पोषक तत्वों का छिड़काव लाभदायक है।"
            elif lang == 'te':
                fertilizer_advice = f"పూత దశ: మంచి పూత కోసం పొటాషియం మరియు బోరాన్ వంటి సూక్ష్మ పోషకాల పిచికారీ ఎంతో మేలు చేస్తుంది."
            else:
                fertilizer_advice = f"Flowering Stage: Foliar application of potassium and essential micronutrients enhances flower retention and pod setting."
    else: # fruiting / maturation
        if lang == 'hi':
            fertilizer_advice = f"फल/दाना पकने की अवस्था: अत्यधिक नाइट्रोजन का उपयोग बंद करें। दानों के वजन और चमक के लिए पोटैशियम का ध्यान रखें।"
        elif lang == 'te':
            fertilizer_advice = f"కాయ/గింజ పక్వ దశ: నత్రజని ఎరువుల వాడకం తగ్గించండి. గింజ నాణ్యత మరియు బరువు కోసం పొటాషియం ఉపయోగపడుతుంది."
        else:
            fertilizer_advice = f"Fruiting/Maturation Stage: Avoid excessive nitrogen late in the season. Ensure adequate potassium for grain filling and quality."

    # Soil type specific modifier
    if soil_type == "sandy":
        if lang == 'hi':
            fertilizer_advice += " (बलुई मिट्टी में पोषक तत्व जल्दी बहते हैं, इसलिए खाद को छोटी-छोटी किस्तों में दें।)"
        elif lang == 'te':
            fertilizer_advice += " (ఇసుక నేలల్లో ఎరువులు త్వరగా కొట్టుకుపోతాయి, కాబట్టి విడతల వారీగా కొద్ది కొద్దిగా వేయండి.)"
        else:
            fertilizer_advice += " (Note: Sandy soils leach nutrients quickly; split application into smaller frequent doses.)"
    elif soil_type == "clay":
        if lang == 'hi':
            irrigation_advice += " (चिकनी मिट्टी में पानी देर तक रुकता है, इसलिए ज्यादा सिंचाई से बचें।)"
        elif lang == 'te':
            irrigation_advice += " (బంకమన్ను నేలల్లో నీరు ఎక్కువ సేపు ఉంటుంది, కాబట్టి అతిగా నీటి తడి ఇవ్వకండి.)"
        else:
            irrigation_advice += " (Note: Clay soil retains water longer; avoid over-watering.)"

    safety_disclaimer = get_translation(lang, 'general_disclaimer') + " " + (
        "नोट: हम सटीक रासायनिक मात्रा की सिफारिश नहीं करते हैं। कृपया अपनी निकटतम कृषि प्रयोगशाला से मिट्टी का परीक्षण करवाएं।" if lang == 'hi' else (
        "గమనిక: మేము ఖచ్చితమైన రసాయన మోతాదులను సూచించము. దయచేసి స్థానిక వ్యవసాయ ల్యాబ్‌లో నేల పరీక్ష చేయించుకోండి." if lang == 'te' else
        "Note: Exact chemical dosages are not provided. Please conduct a soil laboratory test for accurate fertilizer dosage."
    ))

    return {
        'crop_name': crop,
        'moisture': moisture,
        'growth_stage': growth_stage,
        'soil_type': soil_type,
        'irrigation_advice': irrigation_advice,
        'fertilizer_advice': fertilizer_advice,
        'disclaimer': safety_disclaimer
    }

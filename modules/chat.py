from translations import get_translation

def process_chat_message(user_message, lang='en'):
    """
    Offline rule-based NLP chatbot for agricultural guidance.
    Matches key farming terms in English, Hindi, or Telugu.
    """
    if not user_message or not user_message.strip():
        if lang == 'hi':
            return "कृपया अपना खेती से जुड़ा सवाल लिखें (जैसे: सिंचाई, बारिश, गर्मी, खाद या बीमारी)।"
        elif lang == 'te':
            return "దయచేసి మీ వ్యవసాయ సందేహాన్ని టైప్ చేయండి (ఉదా: నీటి తడి, వర్షం, ఎండ, ఎరువులు లేదా తెగుళ్ళు)."
        else:
            return "Please enter a farming question (e.g. irrigation, rain, heat, fertilizer, or crop health)."

    msg = user_message.lower().strip()
    
    # 1. Irrigation & Waterlogging
    if any(k in msg for k in ['irrigation', 'water', 'waterlog', 'सिंचाई', 'पानी', 'जल', 'నీటి', 'తడి', 'నీరు']):
        if any(k in msg for k in ['rain', 'heavy rain', 'बारिश', 'वर्षा', 'వర్షం']):
            if lang == 'hi':
                return "🌧️ **सिंचाई एवं वर्षा सलाह:**\n• यदि भारी बारिश की संभावना है तो सिंचाई तुरंत रोक दें।\n• खेत में पानी जमा न होने दें, ड्रेनेज नालियां खुली रखें।\n*यह एक सामान्य सलाह है।*"
            elif lang == 'te':
                return "🌧️ **నీటి తడి & వర్షపాతం సలహా:**\n• వర్షసూచన ఉన్నప్పుడు పొలానికి నీటి తడి ఇవ్వకండి.\n• పొలంలో నీరు నిలవకుండా బయటకు వెళ్లే కాలువలు సిద్ధంగా ఉంచుకోండి.\n*ఇది సాధారణ సలహా మాత్రమే.*"
            else:
                return "🌧️ **Irrigation & Rain Guidance:**\n• Hold irrigation if heavy rain is expected.\n• Ensure proper drainage channels to prevent waterlogging.\n*General advice only.*"
        else:
            if lang == 'hi':
                return "💧 **सिंचाई सलाह:**\n• सिंचाई हमेशा सुबह तड़के या शाम के समय करें।\n• मिटटी की ऊपरी 2 इंच सतह सूखने पर ही पानी दें।\n• फूल आने की अवस्था में पानी की कमी न होने दें।\n*यह एक सामान्य सलाह है।*"
            elif lang == 'te':
                return "💧 **నీటి తడి సలహా:**\n• తడి ఉదయం లేదా సాయంత్రం వేళల్లోనే ఇవ్వండి.\n• నేల పైపొర ఆరిన తర్వాత మాత్రమే నీటి తడి అందించండి.\n• పూత దశలో నీటి కొరత లేకుండా చూసుకోండి.\n*ఇది సాధారణ సలహా మాత్రమే.*"
            else:
                return "💧 **Irrigation Guidance:**\n• Water crops early morning or late evening.\n• Irrigate only when top 2 inches of soil feel dry.\n• Maintain adequate moisture during flowering.\n*General advice only.*"

    # 2. Heat Stress & Temperature
    elif any(k in msg for k in ['heat', 'temperature', 'sun', '35', 'गर्मी', 'धूप', 'तापमान', 'ఎండ', 'ఉష్ణోగ్రత', 'వేడి']):
        if lang == 'hi':
            return "☀️ **गर्मी व तापमान सुरक्षा:**\n• 35°C से अधिक तापमान होने पर सुबह हल्की सिंचाई करें।\n• छोटे पौधों व नर्सरी पर हल्की शेड नेट का प्रयोग करें।\n• दोपहर के समय रसायन छिड़कने से बचें।\n*यह एक सामान्य सलाह है।*"
        elif lang == 'te':
            return "☀️ **ఎండ & ఉష్ణోగ్రత రక్షణ:**\n• 35°C కంటే ఎక్కువ ఉన్నప్పుడు ఉదయాన్నే తేలికపాటి నీటి తడి ఇవ్వండి.\n• పిందెలు, నాట్లు ఉన్న ప్రాంతంలో నీడ ఏర్పాటు చేయండి.\n• మధ్యాహ్నం వేళ మందులు పిచికారీ చేయవద్దు.\n*ఇది సాధారణ సలహా మాత్రమే.*"
        else:
            return "☀️ **Heat Stress Protection:**\n• Irrigate lightly in the morning when temperature exceeds 35°C.\n• Provide mulch or shade nets for seedlings.\n• Avoid spraying chemicals during peak afternoon heat.\n*General advice only.*"

    # 3. Fertilizer & Soil Nutrition
    elif any(k in msg for k in ['fertilizer', 'compost', 'npk', 'urea', 'खाद', 'उर्वरक', 'यूरिया', 'ఎరువు', 'యూరియా', 'బాస్వరం']):
        if lang == 'hi':
            return "🌱 **खाद एवं पोषण सलाह:**\n• गीली या बारिश वाली मिट्टी में रासायनिक खाद न डालें।\n• वानस्पतिक बढ़वार में नाइट्रोजन और फूल आते समय पोटैशियम दें।\n• रासायनिक मात्रा जानने हेतु निकटतम KVK से मिट्टी परीक्षण करवाएं।\n*यह एक सामान्य सलाह है।*"
        elif lang == 'te':
            return "🌱 **ఎరువుల వాడకం సలహా:**\n• నేల పచ్చిగా ఉన్నప్పుడు లేదా వర్షంలో ఎరువులు వేయకూడదు.\n• శాఖీయ దశలో నత్రజని, పూత దశలో పొటాషియం ఎరువులు వేయాలి.\n• ఖచ్చితమైన మోతాదు కోసం సమీప రైతు సేవా కేంద్రాన్ని సంప్రదించండి.\n*ఇది సాధారణ సలహా మాత్రమే.*"
        else:
            return "🌱 **Fertilizer Advisory:**\n• Do not apply dry fertilizer on waterlogged soil or before heavy rain.\n• Apply nitrogen during vegetative growth and potassium during flowering/fruiting.\n• Conduct a soil lab test for exact chemical dosages.\n*General advice only.*"

    # 4. Crop Health & Disease Symptoms
    elif any(k in msg for k in ['disease', 'spot', 'yellow', 'fungus', 'pest', 'leaf', 'बीमारी', 'कीड़ा', 'पीला', 'पत्ती', 'తెగులు', 'పురుగు', 'ఆకు', 'పసుపు']):
        if lang == 'hi':
            return "🍂 **फसल स्वास्थ्य व बीमारी सलाह:**\n• प्रभावित पत्तियों को तुरंत तोड़कर खेत से बाहर नष्ट करें।\n• नीम तेल (5ml/लीटर पानी) का छिड़काव शुरुआती कीट/फफूंद रोक सकता है।\n• सटीक पहचान के लिए 'Crop Detection' टैब में फोटो अपलोड करें।\n*यह एक सामान्य सलाह है।*"
        elif lang == 'te':
            return "🍂 **పంట ఆరోగ్యం & తెగుళ్ళ సలహా:**\n• తెగులు సోకిన ఆకులను తీసివేసి పొలం బయట నాశనం చేయండి.\n• వేపనూనె (లీటరుకు 5ml) పిచికారీ చేయడం వల్ల ప్రారంభ తెగుళ్ళు తగ్గుతాయి.\n• ఖచ్చితమైన గుర్తింపు కోసం 'Crop Detection' విభాగంలో ఫోటో అప్‌లోడ్ చేయండి.\n*ఇది సాధారణ సలహా మాత్రమే.*"
        else:
            return "🍂 **Crop Health Advisory:**\n• Remove and destroy infected leaves away from the field.\n• Spray Neem oil solution (5ml/L water) for early fungal/pest control.\n• Upload a leaf photo in our 'Crop Detection' module for disease analysis.\n*General advice only.*"

    # 5. Rain & Weather General
    elif any(k in msg for k in ['rain', 'cloud', 'forecast', 'बारिश', 'मौसम', 'वर्षा', 'వర్షం', 'వాతావరణం']):
        if lang == 'hi':
            return "🌧️ **मौसम संबंधी सलाह:**\n• खेत की स्थिति जानने के लिए 'Weather Advice' विकल्प का उपयोग करें।\n• तेज हवा या बारिश में दवाओं का छिड़काव न करें।\n*यह एक सामान्य सलाह है।*"
        elif lang == 'te':
            return "🌧️ **వాతావరణ సలహా:**\n• మీ ప్రాంత వివరాల కోసం 'Weather Advice' విభాగాన్ని చూడండి.\n• ఈదురుగాలులు లేదా వర్షం వచ్చే ముందు మందులు చల్లవద్దు.\n*ఇది సాధారణ సలహా మాత్రమే.*"
        else:
            return "🌧️ **Weather General Advice:**\n• Use our 'Weather Advice' tab for location specific weather guidance.\n• Avoid chemical spraying during windy or rainy weather.\n*General advice only.*"

    # 6. Ambiguous / Unclear query -> Ask clarifying questions
    else:
        if lang == 'hi':
            return (
                "🤖 **अधिक सटीक सलाह के लिए कृपया ये विवरण बताएं:**\n"
                "1. फसल का नाम (उदा. गेहूं, धान, कपास)\n"
                "2. आपका स्थान/शहर\n"
                "3. फसल की अवस्था (अंकुरण, बढ़वार, फूल या फल)\n"
                "4. लक्षण या समस्या (उदा. पत्तियां पीली पड़ना, सूखापन)\n\n"
                "*यह एक ऑफ़लाइन सामान्य सलाह प्रणाली है।*"
            )
        elif lang == 'te':
            return (
                "🤖 **సరైన సలహా కోసం దయచేసి ఈ వివరాలను తెలియజేయండి:**\n"
                "1. పంట పేరు (ఉదా: వరి, మిరప, పత్తి)\n"
                "2. మీ ఊరు / ప్రాంతం\n"
                "3. పంట దశ (మొలక, పెరుగుదల, పూత లేదా కాయ)\n"
                "4. కనిపించే సమస్య (ఉదా: ఆకులు పసుపు రంగులోకి మారడం, ఎండిపోవడం)\n\n"
                "*ఇది ఆఫ్‌లైన్ సాధారణ సలహా వ్యవస్థ.*"
            )
        else:
            return (
                "🤖 **For a more accurate recommendation, please specify:**\n"
                "1. **Crop Name** (e.g. Rice, Wheat, Cotton, Chilli)\n"
                "2. **Location / City**\n"
                "3. **Growth Stage** (Seedling, Vegetative, Flowering, Fruiting)\n"
                "4. **Observed Symptoms** (e.g. yellow leaves, spots, dryness)\n\n"
                "*AgriBridge AI Offline Advisory System.*"
            )

# translations.py - Multilingual Dictionary for AgriBridge AI (en, hi, te)

TRANSLATIONS = {
    'en': {
        # App Info & Brand
        'app_name': 'AgriBridge AI',
        'tagline': 'Real-Time Bridge for Smart Farming Guidance',
        'welcome_title': 'Welcome Farmers!',
        'welcome_subtitle': 'Select a feature below to get personalized, simple, and practical agricultural advice.',
        'demo_mode_badge': 'Demo Mode',
        'live_mode_badge': 'Live Mode',
        'demo_weather_note': 'Demo weather data is being used (API key missing or offline)',
        'general_disclaimer': 'General Guidance Only: Recommendations provided are for informational purposes. Always consult local agricultural experts (KVK) or perform soil tests before major farming decisions.',

        # Navigation
        'nav_home': 'Home',
        'nav_weather': 'Weather Advice',
        'nav_soil': 'Soil Guidance',
        'nav_crop': 'Crop Detection',
        'nav_chat': 'Farming Chat',

        # Feature Card Titles & Descriptions
        'card_weather_title': 'Weather Advice',
        'card_weather_desc': 'Get real-time weather conditions and smart field action advice for your location.',
        'card_soil_title': 'Soil Guidance',
        'card_soil_desc': 'Receive tailored irrigation and general fertilizer advice based on moisture & crop stage.',
        'card_crop_title': 'Crop Disease Detection',
        'card_crop_desc': 'Upload a crop leaf photo to identify diseases and get organic remedy tips.',
        'card_chat_title': 'AI Farming Chat',
        'card_chat_desc': 'Ask questions about crops, rainfall, heat stress, or fertilizers anytime (works offline).',
        'btn_open': 'Open Feature',

        # Weather Page
        'weather_header': 'Weather Advisory',
        'weather_intro': 'Check field weather and receive immediate farming precautions.',
        'lbl_city': 'City / Location Name',
        'ph_city': 'e.g. Hyderabad, Guntur, Nagpur',
        'btn_get_weather': 'Get Weather Advisory',

        # Weather Results
        'res_temperature': 'Temperature',
        'res_humidity': 'Humidity',
        'res_wind_speed': 'Wind Speed',
        'res_weather_desc': 'Condition',
        'res_rain_prob': 'Rain Probability',
        'res_advisory': 'Field Advisory',

        # Soil Page
        'soil_header': 'Soil & Irrigation Guidance',
        'soil_intro': 'Input your field condition to get irrigation and fertilizer recommendations.',
        'lbl_moisture': 'Soil Moisture Level',
        'opt_dry': 'Dry (Low Moisture)',
        'opt_moist': 'Moist (Optimal Moisture)',
        'opt_wet': 'Wet (High Moisture / Waterlogged)',
        'lbl_crop_name': 'Crop Name',
        'ph_crop_name': 'e.g. Rice, Wheat, Cotton, Chilli, Tomato',
        'lbl_growth_stage': 'Growth Stage',
        'opt_seedling': 'Seedling / Early Stage',
        'opt_vegetative': 'Vegetative Growth',
        'opt_flowering': 'Flowering Stage',
        'opt_fruiting': 'Fruiting / Maturation',
        'lbl_soil_type': 'Soil Type (Optional)',
        'opt_soil_any': 'General / Unspecified',
        'opt_clay': 'Clay Soil',
        'opt_loam': 'Loam Soil',
        'opt_sandy': 'Sandy Soil',
        'opt_black': 'Black Cotton Soil',
        'btn_get_soil': 'Get Soil Guidance',

        # Soil Results
        'res_irrigation': 'Irrigation Action',
        'res_fertilizer': 'Fertilizer Guidance',

        # Crop Page
        'crop_header': 'Crop Disease Analyzer (Simulated)',
        'crop_intro': 'Select a clear photo of an affected leaf to identify potential crop diseases.',
        'lbl_upload_image': 'Upload Leaf Photo (JPG, PNG, max 2MB)',
        'lbl_preview': 'Selected Image Preview',
        'btn_analyze_crop': 'Analyze Crop Leaf',
        'crop_simulated_notice': 'This feature provides simulated demo results. Always verify with an agronomist.',

        # Crop Detection Results
        'res_condition': 'Detected Condition',
        'res_confidence': 'Demo Confidence',
        'res_cause': 'Possible Cause',
        'res_treatment': 'Recommended Treatment / Action',
        'res_prevention': 'Preventive Tip',
        'crop_disclaimer': 'This is a demonstration result. Confirm with an expert before applying treatments.',

        # Chat Page
        'chat_header': 'Offline Farming Assistant',
        'chat_intro': 'Ask farming questions in simple English, Hindi, or Telugu.',
        'ph_chat': 'Ask about irrigation, rain, heat, fertilizer, or crop health...',
        'btn_send': 'Send',
        'chat_quick_prompts': 'Quick Questions:',
        'prompt_rain': 'Should I irrigate if heavy rain is expected?',
        'prompt_heat': 'How to protect crops from severe heat above 35°C?',
        'prompt_fertilizer': 'When should I apply fertilizer during flowering?',
        'prompt_disease': 'My plant leaves have yellow spots, what should I do?',
        'chat_welcome_msg': 'Namaste! I am your offline farm assistant. Ask me about irrigation, weather precautions, soil moisture, fertilizers, or plant diseases.',
        'lbl_you': 'You',
        'lbl_assistant': 'Assistant',

        # Result Page Template
        'result_title': 'Advisory Summary',
        'res_feature': 'Module',
        'res_problem': 'Observed Condition / Issue',
        'res_reason': 'Underlying Cause / Context',
        'res_solution': 'Recommended Practical Action',
        'res_tip': 'Preventive Tip',
        'btn_back_home': 'Back to Home',
        'btn_another_search': 'Perform Another Check',

        # Errors & Messages
        'err_404_title': 'Page Not Found (404)',
        'err_404_desc': 'The requested page does not exist or has been moved.',
        'err_500_title': 'Server Error (500)',
        'err_500_desc': 'Something went wrong on our end. Please try again.',
        'err_invalid_city': 'Please enter a valid city or location name.',
        'err_invalid_file': 'Please upload a valid JPG or PNG image under 2MB.',
        'err_file_too_large': 'File size exceeds 2MB limit.',
        'err_no_file': 'No image file was selected.',
    },

    'hi': {
        # App Info & Brand
        'app_name': 'AgriBridge AI',
        'tagline': 'स्मार्ट खेती सलाह के लिए आपका डिजिटल साथी',
        'welcome_title': 'किसान भाइयों का स्वागत है!',
        'welcome_subtitle': 'व्यक्तिगत और व्यावहारिक कृषि सलाह पाने के लिए नीचे दी गई सुविधा चुनें।',
        'demo_mode_badge': 'डेमो मोड',
        'live_mode_badge': 'लाइव मोड',
        'demo_weather_note': 'डेमो मौसम डेटा का उपयोग किया जा रहा है (API कुंजी नहीं मिली या ऑफलाइन)',
        'general_disclaimer': 'केवल सामान्य मार्गदर्शन: दी गई सिफारिशें केवल जानकारी के लिए हैं। किसी भी बड़े फैसले से पहले हमेशा स्थानीय कृषि विशेषज्ञ (KVK) से परामर्श लें या मिट्टी की जांच कराएं।',

        # Navigation
        'nav_home': 'मुख्य पृष्ठ',
        'nav_weather': 'मौसम की सलाह',
        'nav_soil': 'मिट्टी और सिंचाई',
        'nav_crop': 'फसल बीमारी पहचान',
        'nav_chat': 'कृषि चैट',

        # Feature Cards
        'card_weather_title': 'मौसम की सलाह',
        'card_weather_desc': 'अपने स्थान के मौसम की सटीक जानकारी और खेत में ध्यान देने योग्य बातें जानें।',
        'card_soil_title': 'मिट्टी और सिंचाई',
        'card_soil_desc': 'नमी और फसल अवस्था के अनुसार सिंचाई और खाद का सही समय जानें।',
        'card_crop_title': 'फसल बीमारी पहचान',
        'card_crop_desc': 'पत्ती की फोटो अपलोड करें और बीमारी तथा जैविक उपचार की जानकारी पाएं।',
        'card_chat_title': 'कृषि चैट बॉट',
        'card_chat_desc': 'फसल, बारिश, गर्मी या खाद के सवाल कभी भी पूछें (ऑफलाइन भी काम करता है)।',
        'btn_open': 'शुरू करें',

        # Weather Page
        'weather_header': 'मौसम की सलाह',
        'weather_intro': 'अपने स्थान का मौसम देखें और खेती के लिए आवश्यक सावधानियां जानें।',
        'lbl_city': 'शहर / स्थान का नाम',
        'ph_city': 'जैसे: इंदौर, जयपुर, पटना',
        'btn_get_weather': 'मौसम सलाह प्राप्त करें',

        # Weather Results
        'res_temperature': 'तापमान',
        'res_humidity': 'नमी (आर्द्रता)',
        'res_wind_speed': 'हवा की गति',
        'res_weather_desc': 'मौसम की स्थिति',
        'res_rain_prob': 'बारिश की संभावना',
        'res_advisory': 'खेती की सलाह',

        # Soil Page
        'soil_header': 'मिट्टी एवं सिंचाई मार्गदर्शन',
        'soil_intro': 'सिंचाई और खाद की सही सलाह पाने के लिए खेत की स्थिति चुनें।',
        'lbl_moisture': 'मिट्टी में नमी का स्तर',
        'opt_dry': 'सूखी (कम नमी)',
        'opt_moist': 'उपयुक्त नमी (संतुलित)',
        'opt_wet': 'गीली (अधिक जल भराव)',
        'lbl_crop_name': 'फसल का नाम',
        'ph_crop_name': 'जैसे: गेहूं, धान, कपास, मिर्च, टमाटर',
        'lbl_growth_stage': 'फसल की अवस्था',
        'opt_seedling': 'अंकुरण / शुरुआती अवस्था',
        'opt_vegetative': 'बढ़वार / वानस्पतिक अवस्था',
        'opt_flowering': 'फूल आने की अवस्था',
        'opt_fruiting': 'फल / दाना पकने की अवस्था',
        'lbl_soil_type': 'मिट्टी का प्रकार (वैकल्पिक)',
        'opt_soil_any': 'सामान्य / अनिश्चित',
        'opt_clay': 'चिकनी मिट्टी',
        'opt_loam': 'दोमट मिट्टी',
        'opt_sandy': 'बलुई मिट्टी',
        'opt_black': 'काली मिट्टी',
        'btn_get_soil': 'सलाह प्राप्त करें',

        # Soil Results
        'res_irrigation': 'सिंचाई सलाह',
        'res_fertilizer': 'खाद संबंधी मार्गदर्शन',

        # Crop Page
        'crop_header': 'फसल रोग पहचान (सिम्युलेटेड)',
        'crop_intro': 'प्रभावित पत्ती की स्पष्ट फोटो चुनें ताकि बीमारी की पहचान की जा सके।',
        'lbl_upload_image': 'पत्ती की फोटो अपलोड करें (JPG, PNG, अधिकतम 2MB)',
        'lbl_preview': 'चयनित फोटो का पूर्वावलोकन',
        'btn_analyze_crop': 'पत्ती की जांच करें',
        'crop_simulated_notice': 'यह सुविधा डेमो परिणाम प्रस्तुत करती है। अंतिम पुष्टि विशेषज्ञ से करें।',

        # Crop Detection Results
        'res_condition': 'पहचाना गया रोग',
        'res_confidence': 'अनुमानित सटीकता (डेमो)',
        'res_cause': 'संभावित कारण',
        'res_treatment': 'अनुशंसित उपचार / उपाय',
        'res_prevention': 'बचाव के तरीके',
        'crop_disclaimer': 'यह एक प्रदर्शन परिणाम है। उपचार से पहले कृषि विशेषज्ञ से पुष्टि करें।',

        # Chat Page
        'chat_header': 'ऑफलाइन कृषि सहायक',
        'chat_intro': 'सरल भाषा में खेती से जुड़े सवाल पूछें।',
        'ph_chat': 'सिंचाई, बारिश, गर्मी, खाद या बीमारी के बारे में पूछें...',
        'btn_send': 'भेजें',
        'chat_quick_prompts': 'त्वरित प्रश्न:',
        'prompt_rain': 'भारी बारिश की संभावना होने पर क्या सिंचाई करनी चाहिए?',
        'prompt_heat': '35°C से अधिक तापमान पर फसल को कैसे बचाएं?',
        'prompt_fertilizer': 'फूल आने के समय खाद कब देनी चाहिए?',
        'prompt_disease': 'पौधे की पत्तियों पर पीले धब्बे हैं, क्या करें?',
        'chat_welcome_msg': 'नमस्ते! मैं आपका ऑफ़लाइन कृषि सहायक हूँ। सिंचाई, मौसम, मिट्टी की नमी, खाद या फसल बीमारियों के बारे में पूछें।',
        'lbl_you': 'आप',
        'lbl_assistant': 'सहायक',

        # Result Page
        'result_title': 'सलाह सारांश',
        'res_feature': 'मॉड्यूल',
        'res_problem': 'देखी गई स्थिति / समस्या',
        'res_reason': 'मुख्य कारण / संदर्भ',
        'res_solution': 'अनुशंसित व्यावहारिक उपाय',
        'res_tip': 'बचाव की सलाह',
        'btn_back_home': 'मुख्य पृष्ठ पर लौटें',
        'btn_another_search': 'दुबारा जांच करें',

        # Errors
        'err_404_title': 'पृष्ठ नहीं मिला (404)',
        'err_404_desc': 'आपके द्वारा अनुरोधित पृष्ठ मौजूद नहीं है।',
        'err_500_title': 'सर्वर त्रुटि (500)',
        'err_500_desc': 'हमारे सर्वर में कुछ समस्या आई है। कृपया पुनः प्रयास करें।',
        'err_invalid_city': 'कृपया एक वैध शहर या स्थान का नाम दर्ज करें।',
        'err_invalid_file': 'कृपया 2MB से कम की मान्य JPG या PNG फोटो अपलोड करें।',
        'err_file_too_large': 'फ़ाइल का आकार 2MB सीमा से अधिक है।',
        'err_no_file': 'कोई फ़ाइल नहीं चुनी गई।',
    },

    'te': {
        # App Info & Brand
        'app_name': 'AgriBridge AI',
        'tagline': 'రైతు సోదరులకు రియల్-టైమ్ వ్యవసాయ సలహా వేదిక',
        'welcome_title': 'రైతు సోదరులకు స్వాగతం!',
        'welcome_subtitle': 'మీకు అవసరమైన వ్యవసాయ సలహా కోసం కింద ఉన్న విభాగాన్ని ఎంచుకోండి.',
        'demo_mode_badge': 'డెమో మోడ్',
        'live_mode_badge': 'లైవ్ మోడ్',
        'demo_weather_note': 'డెమో వాతావరణ సమాచారం ప్రదర్శించబడుతోంది (API కీ లేదు లేదా ఆఫ్‌లైన్)',
        'general_disclaimer': 'సాధారణ మార్గదర్శకత్వం మాత్రమే: ఇక్కడ ఇచ్చిన సూచనలు అవగాహన కోసం మాత్రమే. ముఖ్యమైన నిర్ణయాలు తీసుకునే ముందు స్థానిక వ్యవసాయ నిపుణులను (KVK) సంప్రదించండి లేదా నేల పరీక్షలు చేయించండి.',

        # Navigation
        'nav_home': 'హోమ్',
        'nav_weather': 'వాతావరణ సలహా',
        'nav_soil': 'నేల & నీటి యాజమాన్యం',
        'nav_crop': 'పంట చీడపీడల గుర్తింపు',
        'nav_chat': 'వ్యవసాయ చాట్',

        # Feature Cards
        'card_weather_title': 'వాతావరణ సలహా',
        'card_weather_desc': 'మీ ప్రాంత వాతావరణ వివరాలు మరియు పంట రక్షణ సలహాలు తెలుసుకోండి.',
        'card_soil_title': 'నేల & నీటి యాజమాన్యం',
        'card_soil_desc': 'నేల తేమ మరియు పంట దశ ఆధారంగా నీటి తడి మరియు ఎరువుల వాడకం సలహాలు.',
        'card_crop_title': 'పంట చీడపీడల గుర్తింపు',
        'card_crop_desc': 'ఆకు ఫోటో అప్‌లోడ్ చేసి తెగుళ్ళ గుర్తింపు మరియు నివారణ ఉపాయాలు పొందండి.',
        'card_chat_title': 'వ్యవసాయ చాట్ బాట్',
        'card_chat_desc': 'పంటలు, వర్షం, ఎండ తీవ్రత లేదా ఎరువుల గురించి ఎప్పుడైనా అడగండి (ఆఫ్‌లైన్‌లో కూడా పనిచేస్తుంది).',
        'btn_open': 'ప్రారంభించండి',

        # Weather Page
        'weather_header': 'వాతావరణ హెచ్చరికలు & సలహాలు',
        'weather_intro': 'మీ గ్రామం/ప్రాంతం పేరు నమోదు చేసి వాతావరణ ఆధారిత సలహాలు పొందండి.',
        'lbl_city': 'నగరం / గ్రామం / ప్రాంతం పేరు',
        'ph_city': 'ఉదా: గుంటూరు, వరంగల్, కర్నూలు',
        'btn_get_weather': 'వాతావరణ వివరాలు పొందు',

        # Weather Results
        'res_temperature': 'ఉష్ణోగ్రత',
        'res_humidity': 'గాలిలో తేమ',
        'res_wind_speed': 'గాలి వేగం',
        'res_weather_desc': 'వాతావరణ పరిస్థితి',
        'res_rain_prob': 'వర్షపాతం సంభావ్యత',
        'res_advisory': 'పంటల భద్రతా సలహా',

        # Soil Page
        'soil_header': 'నేల సారం & నీటి తడి మార్గదర్శి',
        'soil_intro': 'సరైన తడి మరియు ఎరువుల యాజమాన్యం కోసం వివరాలు అందించండి.',
        'lbl_moisture': 'నేలలో తేమ శాతం',
        'opt_dry': 'పొడిగా ఉంది (తక్కువ తేమ)',
        'opt_moist': 'సరిపడా తేమ (అనుకూలం)',
        'opt_wet': 'అధిక తేమ (నీరు నిలిచి ఉంది)',
        'lbl_crop_name': 'పంట పేరు',
        'ph_crop_name': 'ఉదా: వరి, మిరప, పత్తి, మొక్కజొన్న, టమోటా',
        'lbl_growth_stage': 'పంట దశ',
        'opt_seedling': 'మొలక / ప్రారంభ దశ',
        'opt_vegetative': 'శాకీయ పెరుగుదల దశ',
        'opt_flowering': 'పూత దశ',
        'opt_fruiting': 'కాయ / గింజ పక్వ దశ',
        'lbl_soil_type': 'నేల రకం (ఐచ్ఛికం)',
        'opt_soil_any': 'సాధారణం / చెప్పలేదు',
        'opt_clay': 'బంకమన్ను నేల',
        'opt_loam': 'ఒండ్రు నేల',
        'opt_sandy': 'ఇసుక నేల',
        'opt_black': 'నల్లరేగడి నేల',
        'btn_get_soil': 'సలహా పొందు',

        # Soil Results
        'res_irrigation': 'నీటి తడి సలహా',
        'res_fertilizer': 'ఎరువుల వాడకం సలహా',

        # Crop Page
        'crop_header': 'పంట తెగులు గుర్తింపు (సిమ్యులేటెడ్)',
        'crop_intro': 'తెగులు సోకిన ఆకు స్పష్టమైన ఫోటోను ఎంచుకోండి.',
        'lbl_upload_image': 'ఆకు ఫోటో అప్‌లోడ్ చేయండి (JPG, PNG, గరిష్టం 2MB)',
        'lbl_preview': 'ఎంచుకున్న ఫోటో ప్రివ్యూ',
        'btn_analyze_crop': 'పరీక్షించండి',
        'crop_simulated_notice': 'ఇది డెమో ఫలితాలను మాత్రమే చూపుతుంది. నిపుణులతో ధృవీకరించుకోండి.',

        # Crop Detection Results
        'res_condition': 'గుర్తించిన పరిస్థితి / తెగులు',
        'res_confidence': 'డెమో నమ్మకం శాతం',
        'res_cause': 'సంభావ్య కారణం',
        'res_treatment': 'సూచించిన నివారణ చర్య',
        'res_prevention': 'ముందస్తు జాగ్రత్తలు',
        'crop_disclaimer': 'ఇది ప్రదర్శన ఫలితం మాత్రమే. నివారణ మందులు వాడే ముందు వ్యవసాయ నిపుణుడిని సంప్రదించండి.',

        # Chat Page
        'chat_header': 'ఆఫ్‌లైన్ వ్యవసాయ సహాయకుడు',
        'chat_intro': 'తెలుగు, ఇంగ్లీష్ లేదా హిందీలో మీ సందేహాలను అడగండి.',
        'ph_chat': 'నీటి తడి, వర్షం, ఎండ తీవ్రత, ఎరువులు లేదా చీడపీడల గురించి అడగండి...',
        'btn_send': 'పంపు',
        'chat_quick_prompts': 'తక్షణ ప్రశ్నలు:',
        'prompt_rain': 'భారీ వర్ష సూచన ఉన్నప్పుడు నీటి తడి ఇవ్వవచ్చా?',
        'prompt_heat': '35°C కంటే ఎక్కువ ఉష్ణోగ్రత ఉన్నప్పుడు పంటను ఎలా కాపాడుకోవాలి?',
        'prompt_fertilizer': 'పూత దశలో ఎరువులు ఎప్పుడు వేయాలి?',
        'prompt_disease': 'ఆకులపై పసుపు మచ్చలు వచ్చాయి, ఏమి చేయాలి?',
        'chat_welcome_msg': 'నమస్కారం! నేను మీ ఆఫ్‌లైన్ వ్యవసాయ సహాయకుడిని. నీటి తడి, వాతావరణం, నేల తేమ, ఎరువులు లేదా పంట తెగుళ్ళ గురించి అడగండి.',
        'lbl_you': 'మీరు',
        'lbl_assistant': 'సహాయకుడు',

        # Result Page
        'result_title': 'సలహా సారాంశం',
        'res_feature': 'విభాగం',
        'res_problem': 'గమనించిన పరిస్థితి / సమస్య',
        'res_reason': 'మూల కారణం',
        'res_solution': 'సూచించిన పరిష్కారం',
        'res_tip': 'ముందస్తు రక్షణ చిట్కా',
        'btn_back_home': 'హోమ్ పేజీకి వెళ్ళు',
        'btn_another_search': 'మరొక తనిఖీ చేయి',

        # Errors
        'err_404_title': 'పేజీ కనుగొనబడలేదు (404)',
        'err_404_desc': 'మీరు కోరిన పేజీ అందుబాటులో లేదు.',
        'err_500_title': 'సర్వర్ లోపం (500)',
        'err_500_desc': 'సర్వర్‌లో సమస్య ఏర్పడింది. దయచేసి మళ్ళీ ప్రయత్నించండి.',
        'err_invalid_city': 'దయచేసి చెల్లుబాటు అయ్యే నగరం/ప్రాంతం పేరును నమోదు చేయండి.',
        'err_invalid_file': 'దయచేసి 2MB లోపు ఉన్న JPG లేదా PNG ఫోటోను ఎంచుకోండి.',
        'err_file_too_large': 'ఫైల్ పరిమాణం 2MB పరిమితి కంటే ఎక్కువ ఉంది.',
        'err_no_file': 'ఫైల్ ఏదీ ఎంచుకోలేదు.',
    }
}


def get_translation(lang, key, default=None):
    """Retrieve translated text for given lang and key, fallback to 'en', then default or key."""
    if lang not in TRANSLATIONS:
        lang = 'en'
    
    lang_dict = TRANSLATIONS.get(lang, {})
    if key in lang_dict:
        return lang_dict[key]
    
    # Fallback to English dictionary
    en_dict = TRANSLATIONS.get('en', {})
    if key in en_dict:
        return en_dict[key]
    
    return default if default is not None else key

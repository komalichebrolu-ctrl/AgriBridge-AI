import requests
import random
from translations import get_translation

WEATHER_CODES = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Dense Drizzle",
    61: "Slight Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    80: "Slight Rain Showers",
    81: "Moderate Rain Showers",
    82: "Violent Rain Showers",
    95: "Thunderstorm",
}

def get_weather_advisory(city_name, lang='en'):
    """
    Fetches live weather using Open-Meteo API (no API key required)
    or falls back to mock demo data if offline or city is invalid.
    """
    if not city_name or not city_name.strip():
        city_name = "Hyderabad"
    
    city = city_name.strip().title()
    
    weather_data = None
    is_demo = True
    demo_notice = None

    try:
        # Step 1: Geocoding API to convert city to lat & lon (timeout 5s)
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_res = requests.get(geo_url, timeout=5)
        
        if geo_res.status_code == 200:
            geo_data = geo_res.json()
            if 'results' in geo_data and len(geo_data['results']) > 0:
                lat = geo_data['results'][0]['latitude']
                lon = geo_data['results'][0]['longitude']
                resolved_city = geo_data['results'][0].get('name', city)

                # Step 2: Fetch current weather from Open-Meteo Forecast API (timeout 5s)
                weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
                weather_res = requests.get(weather_url, timeout=5)
                
                if weather_res.status_code == 200:
                    w_json = weather_res.json()
                    if 'current_weather' in w_json:
                        cw = w_json['current_weather']
                        temp_c = round(cw['temperature'], 1)
                        wind_speed = round(cw['windspeed'], 1) # km/h
                        w_code = cw.get('weathercode', 0)
                        weather_desc = WEATHER_CODES.get(w_code, "Partly Cloudy")
                        
                        # Infer humidity and rain prob from weathercode for display consistency
                        rain_prob = 80 if w_code in [51, 53, 55, 61, 63, 65, 80, 81, 82, 95] else 15
                        humidity = 85 if rain_prob > 50 else 55

                        weather_data = {
                            'city': resolved_city,
                            'temp_c': temp_c,
                            'humidity': humidity,
                            'wind_speed_kmh': wind_speed,
                            'description': weather_desc,
                            'rain_prob': rain_prob
                        }
                        is_demo = False
    except Exception:
        # Silently catch timeouts, network issues or invalid responses and fall back to demo mode
        pass

    if weather_data is None:
        # Fallback to Demo Mode with stable mock data
        is_demo = True
        demo_notice = get_translation(lang, 'demo_weather_note', 'Demo weather data is being used (API key missing or offline)')
        
        # Use city string hash for consistent demo data
        seed_val = sum(ord(c) for c in city)
        random.seed(seed_val)
        
        mock_temps = [28.5, 36.2, 31.0, 37.8, 26.4]
        mock_hums = [65, 45, 80, 52, 75]
        mock_winds = [12.5, 18.0, 9.5, 22.0, 14.0]
        mock_descs = ['Partly Cloudy', 'Hot Sunny', 'Light Rain Showers', 'Overcast', 'Humid']
        mock_rains = [20, 10, 75, 85, 40]
        
        idx = seed_val % len(mock_temps)
        weather_data = {
            'city': city,
            'temp_c': mock_temps[idx],
            'humidity': mock_hums[idx],
            'wind_speed_kmh': mock_winds[idx],
            'description': mock_descs[idx],
            'rain_prob': mock_rains[idx]
        }
        random.seed()

    # Apply Agronomic Advisory Rules
    advisories = []
    
    # Rule 1: High Rain Probability (>= 70%)
    if weather_data['rain_prob'] >= 70:
        if lang == 'hi':
            advisories.append("भारी बारिश की संभावना (≥70%): सिंचाई को रोकें ताकि जलभराव और जड़ों के सड़ने का खतरा न हो।")
            advisories.append("बारिश के दौरान खाद का प्रयोग न करें ताकि पोषक तत्व बह न जाएं।")
        elif lang == 'te':
            advisories.append("భారీ వర్ష సూచన (≥70%): నీటి తడి ఇవ్వడం నిలిపివేయండి. నీరు నిలిచి వేరు కుళ్ళు తెగులు రాకుండా చూసుకోండి.")
            advisories.append("వర్షం పడే సమయంలో ఎరువులు వేయకూడదు, లేకపోతే పోషకాలు కొట్టుకుపోతాయి.")
        else:
            advisories.append("High rain expected (≥70%): Postpone irrigation to avoid waterlogging and root rot.")
            advisories.append("Avoid applying fertilizers during rain to prevent nutrient runoff.")

    # Rule 2: Heat Stress (> 35°C)
    if weather_data['temp_c'] > 35.0:
        if lang == 'hi':
            advisories.append(f"उच्च तापमान ({weather_data['temp_c']}°C): फसल में गर्मी के तनाव को रोकने के लिए सुबह या शाम हल्की सिंचाई करें।")
        elif lang == 'te':
            advisories.append(f"అధిక ఉష్ణోగ్రత ({weather_data['temp_c']}°C): ఎండ దెబ్బ నుండి కాపాడటానికి ఉదయం లేదా సాయంత్రం వేళల్లో తేలికపాటి నీటి తడి అందించండి.")
        else:
            advisories.append(f"High heat alert ({weather_data['temp_c']}°C): Provide light irrigation early morning or late evening to prevent heat stress.")

    # Rule 3: Normal conditions
    if weather_data['rain_prob'] < 70 and weather_data['temp_c'] <= 35.0:
        if lang == 'hi':
            advisories.append("मौसम सामान्य है: नियमित रूप से खेत का निरीक्षण करें और आवश्यकतानुसार ही सिंचाई करें।")
        elif lang == 'te':
            advisories.append("వాతావరణం సాధారణంగా ఉంది: పొలాన్ని ఎప్పటికప్పుడు గమనిస్తూ అవసరాన్ని బట్టి తడి ఇవ్వండి.")
        else:
            advisories.append("Favorable field weather: Maintain normal crop monitoring and schedule irrigation as per moisture needs.")

    result = {
        'city': weather_data['city'],
        'temp_c': weather_data['temp_c'],
        'humidity': weather_data['humidity'],
        'wind_speed_kmh': weather_data['wind_speed_kmh'],
        'description': weather_data['description'],
        'rain_prob': weather_data['rain_prob'],
        'is_demo': is_demo,
        'badge_text': get_translation(lang, 'demo_mode_badge') if is_demo else get_translation(lang, 'live_mode_badge'),
        'demo_notice': demo_notice,
        'advisories': advisories,
        'disclaimer': get_translation(lang, 'general_disclaimer')
    }
    
    return result


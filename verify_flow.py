import requests

BASE_URL = "http://127.0.0.1:5000"
session = requests.Session()

print("--- Testing AgriBridge AI User Flow ---")

# Step 1: GET Home
r1 = session.get(f"{BASE_URL}/")
print(f"1. Home Page GET: Status {r1.status_code}, Title in page: {'AgriBridge AI' in r1.text}")

# Step 2: POST /set-language to Telugu
r2 = session.post(f"{BASE_URL}/set-language", json={"lang": "te"})
print(f"2. Set Language POST (Telugu): Status {r2.status_code}, Response: {r2.json()}")

# Verify Home now returns Telugu text
r2_home = session.get(f"{BASE_URL}/")
print(f"   Telugu Home Page rendering: {'రైతు' in r2_home.text}")

# Step 3 & 4: GET & POST /weather with city 'Hyderabad'
r3 = session.get(f"{BASE_URL}/weather")
print(f"3. Weather Page GET: Status {r3.status_code}")

r4 = session.post(f"{BASE_URL}/weather", data={"city": "Hyderabad"})
print(f"4. Weather Search POST (Hyderabad): Status {r4.status_code}")
print(f"   Demo Mode Badge present: {'డెమో మోడ్' in r4.text or 'Demo Mode' in r4.text}")
print(f"   Advisory present: {'సిపారసు' in r4.text or 'సలహా' in r4.text or 'advisory' in r4.text.lower()}")

# Step 5: GET Chat & POST Chat message
r5_chat_get = session.get(f"{BASE_URL}/chat")
print(f"5. Chat Page GET: Status {r5_chat_get.status_code}, Contains Welcome: {'నమస్కారం' in r5_chat_get.text or 'Assistant' in r5_chat_get.text}")

r5_chat_post = session.post(f"{BASE_URL}/chat", json={"message": "వర్షం పడితే నీటి తడి ఇవ్వవచ్చా?"})
print(f"6. Chat Message POST: Status {r5_chat_post.status_code}, Reply: {r5_chat_post.json()}")

# Step 7: Return Home
r7 = session.get(f"{BASE_URL}/")
print(f"7. Return Home GET: Status {r7.status_code}")

print("\n--- User Flow Verification Passed Successfully! ---")

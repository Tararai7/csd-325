# api_tutorial.py
# Tara Rai
#CSD-325-M9

import requests
import json

print("=== API Connection Test ===")
# Test basic connection
response = requests.get('http://www.google.com')
print(f"Google connection status: {response.status_code}")

print("\n=== Open Notify API - People in Space ===")
# Get astronaut data from Open Notify API
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

# Test the connection
print(f"API Status Code: {response.status_code}")

# Print raw response (no formatting)
print("\n--- Raw Response (no formatting) ---")
print(response.text)

# Print formatted JSON response (like tutorial)
print("\n--- Formatted JSON Response ---")
def jprint(obj):
    """Pretty print JSON with indentation"""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

# Extract and display astronaut names (tutorial requirement)
print("\n--- Astronauts Currently in Space ---")
data = response.json()
print(f"Total people in space: {data['number']}")
for person in data['people']:
    print(f"  • {person['name']} aboard {person['craft']}")
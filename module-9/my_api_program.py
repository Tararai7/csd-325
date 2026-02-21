# my_api_program.py
# Tara Rai
# CSD-325-9
#Date: 02/20/2026

import requests
import json

print("=== My Custom API Program ===")
print("API: JSONPlaceholder - Sample Post Data")
print("-" * 50)

# Your chosen API endpoint
api_url = "https://jsonplaceholder.typicode.com/posts/1"

# TEST THE CONNECTION (always do this first!)
print("\n[1] Testing API Connection...")
try:
    response = requests.get(api_url, timeout=10)
    print(f"✓ Connection successful! Status Code: {response.status_code}")
except requests.exceptions.Timeout:
    print("✗ Request timed out")
    exit()
except requests.exceptions.RequestException as e:
    print(f"✗ Connection failed: {e}")
    exit()

# PRINT RESPONSE - NO FORMATTING
print("\n[2] Raw Response (no formatting):")
print("-" * 30)
print(response.text)

# PRINT RESPONSE - FORMATTED (like tutorial)
print("\n[3] Formatted JSON Response:")
print("-" * 30)
def jprint(obj):
    """Pretty print JSON with indentation and sorted keys"""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

# BONUS: Extract specific fields (shows you understand the data)
print("\n[4] Extracted Data Fields:")
print("-" * 30)
data = response.json()
print(f"Post ID: {data['id']}")
print(f"User ID: {data['userId']}")
print(f"Title: {data['title']}")
print(f"Body Preview: {data['body'][:100]}...")
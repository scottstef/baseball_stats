import os
import requests

# Get the Datadog API and Application keys directly from the environment variables set by GitHub Actions secrets
DD_API_KEY = os.getenv('DD_API_KEY')
DD_APP_KEY = os.getenv('DD_APP_KEY')

if not DD_API_KEY or not DD_APP_KEY:
    print("Error: Datadog API key or Application key not found.")
    exit(1)

# Use a proper API endpoint for Datadog
url = "https://api.datadoghq.com/api/v1/check_run"  # Replace this with the correct API endpoint you need

# Set up headers for authentication
headers = {
    "DD-API-KEY": DD_API_KEY,
    "DD-APPLICATION-KEY": DD_APP_KEY
}

# Try to connect to Datadog API
try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Successfully connected to Datadog API!")
    else:
        print(f"Failed to connect to Datadog API. Status code: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error connecting to Datadog API: {e}")

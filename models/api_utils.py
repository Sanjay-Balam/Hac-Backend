import os
import requests

# Set Google Bard API Key from environment variables (set directly in code for now)
API_KEY = "AIzaSyA7KBSVOz1xTKq8-4oLczseKZ5ORVS0c88"

# Define the Google Bard API endpoint
BARD_API_URL = "https://bard.googleapis.com/v1/generate"


def get_bard_response(prompt):
    """Generate a Socratic question using Google Bard API."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Payload for the API request
    data = {
        "prompt": prompt,
        "max_tokens": 150,  # Set max token length if supported
        "temperature": 0.7  # Set temperature to control randomness
    }

    # Make a POST request to Google Bard API
    response = requests.post(BARD_API_URL, headers=headers, json=data)

    # Check for a successful response
    if response.status_code == 200:
        response_data = response.json()
        # Assuming the response JSON contains a 'text' field for the generated answer
        return response_data.get("text", "No response generated.")
    else:
        # If the response fails, return an error message
        return f"Error: {response.status_code}, {response.text}"

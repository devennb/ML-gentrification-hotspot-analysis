import requests
import json


def nearby_search(api_key, latitude, longitude, radius, types):
    url = "https://places.googleapis.com/v1/places:searchNearby"
    headers = {
      "Content-Type": "application/json",
      "X-Goog-Api-Key": api_key,
      "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.types,places.reviews,places.priceLevel"
    }
    payload = {
      "includedTypes": types,
      "maxResultCount": 20,
      "locationRestriction": {
          "circle": {
              "center": {
                  "latitude": latitude,
                  "longitude": longitude
              },
              "radius": radius
            }
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json().get("places", [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
  
def text_search(api_key, text):
    url = "https://places.googleapis.com/v1/places:searchText"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.types,places.reviews,places.priceLevel"
    }

    payload = {
        "textQuery" : text.lower()
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json().get("places", [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
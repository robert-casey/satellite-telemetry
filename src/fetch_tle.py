import requests
import json
import os
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

USERNAME = os.getenv("SPACETRACK_USER")
PASSWORD = os.getenv("SPACETRACK_PASS")

# Space-Track API base URLs
BASE_URL = "https://www.space-track.org"
LOGIN_URL = f"{BASE_URL}/ajaxauth/login"
TLE_URL = f"{BASE_URL}/basicspacedata/query/class/tle_latest/NORAD_CAT_ID/25544/orderby/EPOCH desc/limit/1/format/json"

def fetch_tle():
    with requests.Session() as session:

        # Step 1: Authenticate
        login_payload = {
            "identity": USERNAME,
            "password": PASSWORD
        }
        login_response = session.post(LOGIN_URL, data=login_payload)

        if login_response.status_code != 200:
            print(f"Login failed: {login_response.status_code}")
            return

        print("Login successful.")

        # Step 2: Fetch TLE data
        tle_response = session.get(TLE_URL)

        if tle_response.status_code != 200:
            print(f"TLE fetch failed: {tle_response.status_code}")
            return

        # Step 3: Parse and display
        tle_data = json.loads(tle_response.text)
        print(json.dumps(tle_data, indent=2))

        # Step 4: Save raw response to file
        os.makedirs("data", exist_ok=True)
        with open("data/tle_raw.json", "w") as f:
            json.dump(tle_data, f, indent=2)

        print("Data saved to data/tle_raw.json")

if __name__ == "__main__":
    fetch_tle()

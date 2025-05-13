import os
import time
import hmac
import hashlib
import base64
import requests

ACCESS_KEY = os.getenv("ONSHAPE_ACCESS_KEY")
SECRET_KEY = os.getenv("ONSHAPE_SECRET_KEY")
BASE_URL = "https://cad.onshape.com"
METHOD = "GET"
URL_PATH = "/api/users/sessioninfo"

date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
hmac_data = f"(request-target): {METHOD.lower()} {URL_PATH}\ndate: {date}"

signature = base64.b64encode(
    hmac.new(SECRET_KEY.encode('utf-8'), hmac_data.encode('utf-8'), hashlib.sha256).digest()
).decode('utf-8')

headers = {
    'Authorization': f'On {ACCESS_KEY}:HmacSHA256:{signature}',
    'Date': date
}

response = requests.get(BASE_URL + URL_PATH, headers=headers)

print("Status code:", response.status_code)
print("Response body:", response.text)

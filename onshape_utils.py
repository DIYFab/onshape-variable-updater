import hashlib
import hmac
import base64
import time
import os

ACCESS_KEY = "Vt89PRMzzCpHYbsKkRxfgcXH"
SECRET_KEY = "MOVFDfYg673RAoIt2xJfljhLXSpui1OfFB58lOy0sltWoHXM"
BASE_URL = "https://cad.onshape.com"


def create_headers(method, url_path):
    date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
    hmac_data = f'(request-target): {method.lower()} {url_path}\ndate: {date}'

    print("Current time:", time.time())
    print("\n--- HMAC DEBUG ---")
    print("Method:", method)
    print("URL Path:", url_path)
    print("Date:", date)
    print("HMAC String:\n", hmac_data)
    print("Access Key:", ACCESS_KEY[:6] + "..." if ACCESS_KEY else "None")
    print("Secret Key:", "SET" if SECRET_KEY else "None")
    print(f"Access key repr: {repr(ACCESS_KEY)}")
    print(f"Secret key repr: {repr(SECRET_KEY)}")


    signature = base64.b64encode(
        hmac.new(SECRET_KEY.encode('utf-8'), hmac_data.encode('utf-8'), digestmod=hashlib.sha256).digest()
    ).decode('utf-8')

    headers = {
        'Authorization': f'On {ACCESS_KEY}:HmacSHA256:{signature}',
        'Date': date,
        'Content-Type': 'application/json'
    }

    print("Authorization Header:\n", headers["Authorization"])
    print("--- END DEBUG ---\n")

    return headers



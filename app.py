from flask import Flask, request, jsonify
import requests
from onshape_utils import create_headers, BASE_URL



app = Flask(__name__)

# Onshape document details
DID = "2885bf9a2838dbeba18fc91b"
WID = "cd97436ed0757fca074ab317"
EID = "f603c2512efe634d17ce3ef8"

@app.route('/update-variables', methods=['POST'])
def update_variables():
    data = request.get_json()
    cap_od = data['cap_od']
    detent_distance = data['detent_distance']
    detent_od = data['detent_od']

    try:
        url_path = f"/api/partstudios/d/{DID}/w/{WID}/e/{EID}/variables"
        headers = create_headers("POST", url_path)
        response = requests.post(
            BASE_URL + url_path,
            headers=headers,
            json={
                "variables": [
                    {"name": "Wheel_Cap_OD", "value": cap_od},
                    {"name": "Distance_to_Detent", "value": detent_distance},
                    {"name": "Wheel_Cap_Detent_OD", "value": detent_od}
                ]
            }
        )
        response.raise_for_status()
        return jsonify({"message": "Variables updated successfully!"})

    except requests.exceptions.RequestException as e:
        print("Onshape API error:", e.response.text)
        return jsonify({"error": "Failed to update variables"}), 500

if __name__ == '__main__':
    app.run(debug=True)

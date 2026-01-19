from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('waste_data.json', 'r') as f:
    waste_db = json.load(f)

def classify_waste(item_name):
    item_name = item_name.lower()
    for category, items in waste_db.items():
        for item, info in items.items():
            if item_name in item:
                return category, info
    return None, None

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_input = data.get('item', '')

    category, info = classify_waste(user_input)

    if category:
        response = {
            'item': user_input,
            'category': category,
            'instruction': info['instruction'],
            'tip': info['tip']
        }
    else:
        response = {
            'item': user_input,
            'category': 'Unknown',
            'instruction': 'Item not found. Please contact local municipality for disposal guidance.',
            'tip': 'Try to avoid mixing hazardous waste with household waste.'
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

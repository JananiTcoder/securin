import json
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

with open('US_recipes_null.json', 'r', encoding='utf-8') as f:
    recipes = json.load(f)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('text', '').strip().lower()
    if not query:
        return jsonify([])

    results = []
    for item in recipes.values():
        title = str(item.get('title', '')).strip().lower()
        if title == query:
            results.append(item)
            break

    if not results:
        for item in recipes.values():
            if query in str(item.get('title', '')).lower() or query in str(item.get('cuisine', '')).lower() or query in str(item.get('Country_State', '')).lower() or query in str(item.get('Contient', '')).lower():
                results.append(item)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)



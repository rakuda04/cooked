from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data
recipes = [
    {
        "id": 1,
        "title": "Asian white noodle with extra seafood",
        "author": "Suhayb",
        "time": "20 Min",
        "kcal": "",
        "category": "Featured",
        "image": "https://placehold.co/264x172"
    },
    {
        "id": 2,
        "title": "Healthy Taco Salad with fresh vegetable",
        "author": "Betty",
        "time": "20 Min",
        "kcal": "120 Kcal",
        "category": "Breakfast",
        "image": "https://placehold.co/200x240"
    },
    {
        "id": 3,
        "title": "Japanese-style Pancakes Recipe",
        "author": "Jane",
        "time": "12 Min",
        "kcal": "64 Kcal",
        "category": "Breakfast",
        "image": "https://placehold.co/200x240"
    }
]

@app.route("/api/recipes", methods=["GET"])
def get_all_recipes():
    return jsonify(recipes)

@app.route("/api/recipes/<string:category>", methods=["GET"])
def get_recipes_by_category(category):
    filtered = [r for r in recipes if r["category"].lower() == category.lower()]
    return jsonify(filtered)

@app.route("/api/recipe/<int:recipe_id>", methods=["GET"])
def get_recipe_by_id(recipe_id):
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    return jsonify({"error": "Recipe not found"}), 404

@app.route("/api/recipes", methods=["POST"])
def add_recipe():
    data = request.get_json()
    new_id = max(r['id'] for r in recipes) + 1
    data['id'] = new_id
    recipes.append(data)
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)

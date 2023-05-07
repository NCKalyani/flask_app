from flask import Flask, jsonify, request, url_for
from http import HTTPStatus
from flask_restful import Resource
from models.recipe import Recipe, recipes_list



@app.route("/")
def home():
    return "<h1>welcome to cooking page</h1>"


recipes = [
    {"id": 1,
     "name": "tomato soup",
     "description": "This is a lovely tomato soup"},
    {"id": 2,
     "name": "egg salad",
     "description": "this is a tasty egg salad"}
]


@app.route('/recipes', methods=["GET"])
def get_recipes():
    return jsonify({"data": recipes})


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND


@app.route('/recipes', methods=['POST'])
def create_recipe():
    recipe = {
      'id': len(recipes) + 1,
      'name': request.args.get('name'),
      'description': request.args.get('description')
    }
    recipes.append(recipe)
    return jsonify(recipe), HTTPStatus.CREATED


@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
        data = request.get_json()
        recipe.update(
  {
   'name': data.get('name'),
   'description': data.get('description')
  }
       )
    return jsonify(recipe)


if __name__ == '__main__':
    app.run()

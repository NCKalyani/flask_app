from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.recipe import Recipe, recipes_list


class RecipeListResource(Resource):

    def get(self):
        data = []
        for recipe in recipes_list:
            if recipe.is_published is True:
                data.append(recipe.data)
        return {'data': data},HTTPStatus.OK

    def post(self):
        data = request.get_json()
        recipe = Recipe(name=data['name'],
                        description=data['description'],
                        number_of_serving=data['number_of_serving'],
                        directions=data['directions'],
                        cooking_time=data['cooking_time'])
        recipes_list.append(recipe)
        return recipe.data,HTTPStatus.CREATED

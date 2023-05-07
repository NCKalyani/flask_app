recipes_list = []


def get_last_id():
    if recipes_list:
        last_recipe = recipes_list[-1]
    else:
        return 1
    return last_recipe.id + 1


class Recipe:
    def __init__(self, number_of_serving, name, description, cooking_time, directions):
        self.id = get_last_id()
        self.name = name
        self.description = description
        self.number_of_serving = number_of_serving
        self.description = description
        self.cooking_time = cooking_time
        self.is_published = False
        self.directions = directions

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'number_of_serving': self.number_of_serving,
            'cooking_time': self.cooking_time,
            'directions': self.directions
        }

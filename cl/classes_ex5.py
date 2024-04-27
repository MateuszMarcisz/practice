# NEEDS TO BE FINISHED

class Ingredient:
    def __init__(self, name, proteins, carbs, fats):
        self.name = name
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats


class Meal:
    def __init__(self, name):
        self.name = name
        self.ingredients = {}

    def add_ingredient(self, ingredient, amount):
        if ingredient.name not in self.ingredients:
            self.ingredients[ingredient.name] = {'amount': amount, 'ingredient': ingredient}
        else:
            self.ingredients[ingredient.name]['amount'] += amount


class DailyPlan:
    def __init__(self, name):
        self.name = name
        self.meals = []

    def add_meal(self, meal):
        self.meals.append(meal)

# NEEDS TO BE FINISHED

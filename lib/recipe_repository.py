from lib.recipe import Recipe

class RecipeRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            item = Recipe(row["id"], row["recipe_name"], row["cooking_time"], row["rating"])
            recipes.append(item)
        return recipes

    def find(self, recipe_name):
        rows = self.connection.execute(
            'SELECT * from recipes WHERE id = %s', [recipe_name])
        row = rows[0]
        return Recipe(row["id"], row["recipe_name"], row["cooking_time"], row["rating"])
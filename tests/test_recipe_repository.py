from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

def test_get_all_recipes(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repository = RecipeRepository(db_connection)

    recipes = repository.all()

    assert recipes == [
        Recipe(1, 'Mac and Cheese', 20, 5),
        Recipe(2, 'Pizza', 15, 5),
        Recipe(3, 'Lasagne', 45, 4),
        Recipe(4, 'Jacket Potato', 50, 1),
        Recipe(5, 'Roast Beef', 120, 3)
    ]


def test_get_single_record(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repository = RecipeRepository(db_connection)

    recipe = repository.find(4)
    assert recipe == Recipe(4, 'Jacket Potato', 50, 1)
from lib.recipe import Recipe

def test_recipe_constructs():
    recipe = Recipe(1, 'Mac and Cheese', 20, 5)
    assert recipe.id == 1
    assert recipe.recipe_name == 'Mac and Cheese'
    assert recipe.cooking_time == 20
    assert recipe.rating == 5


def test_equal():
    recipe_1 = Recipe(1, "Mac and Cheese", 20, 5)
    recipe_2 = Recipe(1, "Mac and Cheese", 20, 5)
    assert recipe_1 == recipe_2

def test_format():
    recipe = Recipe(1, 'Mac and Cheese', 20, 5)
    assert str(recipe) == 'Recipe(1, Mac and Cheese, 20, 5)'
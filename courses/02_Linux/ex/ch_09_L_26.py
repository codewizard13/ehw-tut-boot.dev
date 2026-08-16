# def check_ingredient_match(recipe, ingredients):
    
#     ingredients_found = 0
#     missing_ingredients = []

#     for i in range(len(ingredients)):
#         print(f"Ingredient {i}: {ingredients[i]}")

#         if ingredients[i] in recipe:
#             ingredients_found += 1
#         else:
#             missing_ingredients.append(ingredients[i])

#     percentage = (ingredients_found / len(recipe)) * 100

#     return percentage, missing_ingredients
        

def check_ingredient_match(recipe, ingredients):
    
    ingredients_found = 0
    missing_ingredients = []

    for i in range(len(recipe)):
        print(f"Ingredient {i}: {recipe[i]}")

        if recipe[i] in ingredients:
            ingredients_found += 1
        else:
            missing_ingredients.append(recipe[i])

    percentage = (ingredients_found / len(recipe)) * 100

    return percentage, missing_ingredients







recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
ingredients = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]

percentage, missing_ingredients = check_ingredient_match(recipe, ingredients)
print(percentage, missing_ingredients)
# Prints: 75.00 ["Unicorn Hair"]
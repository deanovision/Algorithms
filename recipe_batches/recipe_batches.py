#!/usr/bin/python

import math


# def recipe_batches(recipe, ingredients):
#     max_whole_batches = 0
#     # loop through ingredients and check if the matching key value in recipe is equal or greater
#     for ingredient_name, amount in ingredients.items():
#         # if greater divide key value on ingredients by key value on recipe to max batches from that one ingredients
#         if ingredients[ingredient_name] >= recipe[ingredient_name]:
#             # setup variable to track max batches, keep the lowest max batch number from all ingredients
#             # and return that number
#             if max_whole_batches == 0:
#             max_whole_batches = amount > recipe[ingredient_name] // 2
#             elif max

#     return max_whole_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

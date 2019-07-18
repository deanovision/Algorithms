#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    # loop through ingredients and check if the matching key value in recipe is equal or greater
    max_whole_batches = None
    for ingredient_name, amount in recipe.items():
        # if greater divide key value on ingredients by key value on recipe to max batches from that one ingredients
        try:
            if ingredients[ingredient_name] >= recipe[ingredient_name]:
                # setup variable to track max batches, keep the lowest max batch number from all ingredients
                # and return that number
                if max_whole_batches == None:
                    max_whole_batches = ingredients[ingredient_name] // amount
                elif max_whole_batches > ingredients[ingredient_name] // amount:
                    max_whole_batches = ingredients[ingredient_name] // amount
        except KeyError:
            max_whole_batches = 0
            return max_whole_batches
    return max_whole_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    # recipe = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
    # ingredients = {'milk': 1288, 'flour': 9, 'sugar': 95}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

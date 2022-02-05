def recipeQuery(displayFields):
    query = f"""SELECT {displayFields} from recipe
INNER JOIN brewnote ON recipe.id=brewnote.recipe_id
INNER JOIN fermentable_in_recipe ON fermentable_in_recipe.recipe_id=recipe.id
INNER JOIN fermentable ON fermentable.id=fermentable_in_recipe.fermentable_id
WHERE
NOT recipe.folder='brewtarget'
AND recipe.deleted='0'
AND brewnote.deleted='0'
GROUP BY brewnote.id
ORDER BY recipe.name,brewnote.brewDate
"""
    return query
    


# SELECT recipe.name,group_concat(fermentable.name || ' [' || fermentable.amount || ' kg]',', ') from recipe
# INNER JOIN brewnote ON recipe.id=brewnote.recipe_id
# INNER JOIN fermentable_in_recipe ON fermentable_in_recipe.recipe_id=recipe.id
# INNER JOIN fermentable ON fermentable.id=fermentable_in_recipe.fermentable_id
# WHERE
# NOT recipe.folder='brewtarget'
# AND recipe.deleted='0'
# AND brewnote.deleted='0'
# GROUP BY brewnote.id
# ORDER BY recipe.name,brewnote.brewDate

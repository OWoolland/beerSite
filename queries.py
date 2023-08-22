def mainQuery(fields):
    query = f"""SELECT {fields} from recipe
INNER JOIN brewnote ON recipe.id=brewnote.recipe_id
WHERE
recipe.deleted='0'
AND brewnote.display='1'
GROUP BY brewnote.id, recipe.name
ORDER BY recipe.name,brewnote.brewDate
"""
    return query

def ingredientQuery(ingredient):
    fields = ingredient[0]
    type = ingredient[1]
    
    query = f"""SELECT {fields}
from recipe
LEFT JOIN brewnote ON recipe.id=brewnote.recipe_id
LEFT JOIN {type}_in_recipe ON {type}_in_recipe.recipe_id=recipe.id
LEFT JOIN {type} ON {type}.id={type}_in_recipe.{type}_id
WHERE
recipe.deleted='0'
AND brewnote.display='1'
GROUP BY brewnote.id,recipe.name
ORDER BY recipe.name,brewnote.brewDate
"""
    return query
    


# SELECT recipe.id,recipe.name,brewnote.brewDate,brewnote.og,brewnote.abv,
# group_concat(fermentable.name || ' [' || fermentable.amount || ' kg]',', '),
# group_concat(hop.name || ' [' || hop.amount || ' kg @ ' || hop.time || ']',', ')  
# from recipe
# INNER JOIN brewnote ON recipe.id=brewnote.recipe_id
# INNER JOIN fermentable_in_recipe ON fermentable_in_recipe.recipe_id=recipe.id
# INNER JOIN fermentable ON fermentable.id=fermentable_in_recipe.fermentable_id
# INNER JOIN hop_in_recipe ON hop_in_recipe.recipe_id=recipe.id
# INNER JOIN hop ON hop.id=hop_in_recipe.hop_id
# WHERE
# NOT recipe.folder='brewtarget'
# AND recipe.deleted='0'
# AND brewnote.deleted='0'
# GROUP BY brewnote.id
# ORDER BY recipe.name,brewnote.brewDate

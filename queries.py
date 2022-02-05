def recipeQuery(displayFields):
    query = f"""SELECT {displayFields} from recipe
INNER JOIN brewnote ON recipe.id=brewnote.recipe_id
WHERE
NOT recipe.folder='brewtarget'
AND recipe.deleted='0'
AND brewnote.deleted='0'
ORDER BY recipe.name"""

    return query
    

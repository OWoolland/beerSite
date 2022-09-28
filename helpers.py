import sqlite3 as sql
import pandas as pd

import queries
import minio_helpers as mh

recipeRounding = {
    'OG': '{:.3f}',
    'ABV %': '{:.1f}',
    'Quantity (kg)': '{:.2f}'
    }

main_columns = {
    #"recipe.id"         : "ID",
    "recipe.name"       : "Name",
    "brewnote.brewDate" : "Date Brewed",
    #"brewnote.og"       : "OG",
    "brewnote.abv"      : "ABV %"
    }

# intregients = {
#     'Fermentable' : ['name',' [','amount', etc] 
# }

delim = "'<br> '"
ingredient_columns = {
    f"group_concat(fermentable.name || ' [' || fermentable.amount || ' kg]',{delim})"            : "Fermentable",
    f"group_concat(hop.name || ' [' || (hop.amount*1000) || ' g @ ' || hop.time || ']',{delim})" : "Hop",
    f"group_concat(misc.name || ' [' || misc.use|| ' ' || (misc.amount*1000) || ' g]',{delim})"  : "Misc",
    f"group_concat(yeast.name,{delim})" : "Yeast",
}

def getRecipies():

    # --------------------------------------------------------------------------
    # Get database from minio

    mh.getDatabaseFile()
    
    # --------------------------------------------------------------------------
    # Connect to database
    
    connection = sql.connect('./database.sqlite')
    cursor = connection.cursor()

    displayFields = ','.join(main_columns.keys())

    query = queries.mainQuery(displayFields)
    main = pd.read_sql_query(query, connection)
    column_names = list(main_columns.values())
    
    recipies = main
    for ingredient in ingredient_columns.items():
        query = queries.ingredientQuery(ingredient)
        result = pd.read_sql_query(query, connection)

        recipies = recipies.join(result)
        column_names.append(ingredient[1])

    recipies.columns = column_names

    recipies['Date Brewed'] = pd.to_datetime(recipies['Date Brewed'])
    recipies['Date Brewed'] = recipies['Date Brewed'].dt.strftime('%Y-%m-%d')

    recipies = recipies.style.format(recipeRounding).to_html()

    connection.close()
    return recipies

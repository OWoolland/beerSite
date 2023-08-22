import psycopg2
import pandas as pd

import queries

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
    f"string_agg(fermentable.name || ' [' || fermentable.amount || ' kg]',{delim})"            : "Fermentable",
    f"string_agg(hop.name || ' [' || (hop.amount*1000) || ' g @ ' || hop.time || ']',{delim})" : "Hop",
    f"string_agg(misc.name || ' [' || misc.use|| ' ' || (misc.amount*1000) || ' g]',{delim})"  : "Misc",
    f"string_agg(yeast.name,{delim})" : "Yeast",
}

def getRecipies():

    # --------------------------------------------------------------------------
    # Connect to database
    
    connection = psycopg2.connect(
        host="localhost",
        database="brewtarget",
        user="brewtarget",
        password="brewtarget")

    cursor = connection.cursor()

    # --------------------------------------------------------------------------
    # Form query for columns of simple parameters

    # Get fields
    displayFields = ','.join(main_columns.keys())

    # Perform query
    query = queries.mainQuery(displayFields)
    main = pd.read_sql_query(query, connection)

    # Extract column names
    column_names = list(main_columns.values())

    # --------------------------------------------------------------------------
    # Form queries for complex parameters
    # (many parameters joined in single column)
    
    recipies = main

    # Iterate over paremeters
    for ingredient in ingredient_columns.items():
        # Fetch amalgamated ingredient details
        query = queries.ingredientQuery(ingredient)
        result = pd.read_sql_query(query, connection)

        # Append to tabular form
        recipies = pd.concat([recipies,result], axis=1)
        column_names.append(ingredient[1])

    # --------------------------------------------------------------------------
    # Name table columns

    recipies.columns = column_names

    # --------------------------------------------------------------------------
    # Postprocess datetimes

    recipies['Date Brewed'] = pd.to_datetime(recipies['Date Brewed'])
    recipies['Date Brewed'] = recipies['Date Brewed'].dt.strftime('%Y-%m-%d')

    # --------------------------------------------------------------------------
    # Round values in all columns

    recipies = recipies.style.format(recipeRounding).to_html()

    # --------------------------------------------------------------------------
    # Close db connection

    connection.close()
    return recipies

import streamlit as st
import sqlite3 as sql
import pandas as pd

import queries 

recipeRounding = {
    'OG': '{:.3f}',
    'ABV %': '{:.1f}',
    'Quantity (kg)': '{:.2f}'
    }

main_columns = {
    "recipe.id"         : "ID",
    "recipe.name"       : "Name",
    "brewnote.brewDate" : "Date Brewed",
    "brewnote.og"       : "OG",
    "brewnote.abv"      : "ABV %"
    }

ingredient_columns = {
    "group_concat(fermentable.name || ' [' || fermentable.amount || ' kg]',', ')" : "Fermentable",
    "group_concat(hop.name || ' [' || hop.amount || ' kg @ ' || hop.time || ']')" : "Hop"
}

def getRecipies():
    connection = sql.connect('database.sqlite')
    cursor = connection.cursor()

    displayFields = ','.join(main_columns.keys())

    query = queries.mainQuery(displayFields)
    main = pd.read_sql_query(query, connection)
    main.columns = main_columns.values()

    recipies = main
    for ingredient in ingredient_columns.items():
        query = queries.ingredientQuery(ingredient)
        result = pd.read_sql_query(query, connection)

        recipies = recipies.join(result)

    
    

    recipies['Date Brewed'] = pd.to_datetime(recipies['Date Brewed'])
    recipies['Date Brewed'] = recipies['Date Brewed'].dt.strftime('%Y-%m-%d')

    recipies = recipies.style.format(recipeRounding)

    connection.close()
    return recipies

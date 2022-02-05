import streamlit as st
import sqlite3 as sql
import pandas as pd

import queries 

recipeRounding = {
    'OG': '{:.3f}',
    'ABV %': '{:.1f}'
    }

columns = {
    "recipe.id"         : "ID",
    "recipe.name"       : "Name",
    "brewnote.brewDate" : "Date Brewed",
    "brewnote.og"       : "OG",
    "brewnote.abv"      : "ABV %"
    }

def getRecipies():
    connection = sql.connect('database.sqlite')
    cursor = connection.cursor()

    displayFields = ','.join(columns.keys())
    query = queries.recipeQuery(displayFields)

    recipies = pd.read_sql_query(query, connection)
    recipies.columns = columns.values()

    recipies['Date Brewed'] = pd.to_datetime(recipies['Date Brewed'])
    recipies['Date Brewed'] = recipies['Date Brewed'].dt.strftime('%Y-%m-%d')

    recipies = recipies.style.format(recipeRounding)

    connection.close()
    return recipies

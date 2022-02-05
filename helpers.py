import streamlit as st
import sqlite3 as sql
import pandas as pd

import queries 

def getRecipies():
    connection = sql.connect('database.sqlite')
    cursor = connection.cursor()

    displayFields = "recipe.id,recipe.name," \
        "brewnote.brewDate,brewnote.og,brewnote.abv"
    query = queries.recipeQuery(displayFields)

    recipies = pd.read_sql_query(query, connection)

    connection.close()
    return recipies

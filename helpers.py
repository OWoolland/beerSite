import streamlit as st
import sqlite3 as sql
import pandas as pd

def getRecipies():
    connection = sql.connect('database.sqlite')
    cursor = connection.cursor()

    displayFields = "recipe.id,recipe.name," \
        "brewnote.brewDate,brewnote.og,brewnote.abv"
    query = "SELECT " + displayFields + " from recipe" \
        " INNER JOIN brewnote ON recipe.id=brewnote.recipe_id " \
        " WHERE" \
        " NOT recipe.folder='brewtarget'" \
        " AND recipe.deleted='0'" \
        " AND brewnote.deleted='0' " \
        " ORDER BY recipe.name"

    recipies = pd.read_sql_query(query, connection)

    connection.close()
    return recipies

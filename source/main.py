import lib
import sqlite3 as sq3 
import eel

con= sq3.connect("source/recipes.db") 
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS recipes(name, ingredients, instructions)")
cur.execute("CREATE TABLE IF NOT EXISTS ingredients(name PRIMARY KEY,is_in_cupboard)")

while (True):

    selection=input(""""Choose function: insert recipe, delete recipe, see recipes, insert ingredient, delete ingredient, see ingredients, see suggestions, exit program""")

    match selection:
        case '1':
            lib.insert_recipe(con,cur)
        case '2':
            lib.delete_recipe(con,cur)
        case '3':
            lib.see_recipes(con,cur)
        case '4':
            lib.insert_ingredient(con,cur)
        case '5':
            lib.delete_ingredient(con,cur)
        case '6':
            lib.see_ingredients(con,cur)
        case '7':
            lib.see_sugestions(con,cur)   
        case '8':
            break
        case '9':
            lib.see_data(con,cur)
        case _ :
            print("Function not found")






import lib
import sqlite3 as sq3 
import eel

con= sq3.connect("./data/recipes.db") 
cur=con.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS recipes(quantities, measures, ingredients, howto)")
cur.execute("CREATE TABLE IF NOT EXISTS recipes(name,ingredients, howto)")
cur.execute("CREATE TABLE IF NOT EXISTS ingredients(name)")

while (True):

    selection=input(""""Choose function: insert recipe, delete recipe, see recipes, insert ingredient, delete ingredient, see ingredients, exit program""")

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
        #case '7':
        #    lib.see_sugestions(con,cur)   
        case '7':
            break
        case _ :
            print("Function not found")



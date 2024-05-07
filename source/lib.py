import sqlite3 as sq3
import re 

def insert_recipe(con,cur):
    recipe_name=input("What is the name of the recipe? ")
    ingredients=input("What are the ingredients of the recipe? ")
    instructions=input("What are the instructions? ")
    cur.execute(""" SELECT name
                    FROM recipes
                    WHERE name=?""",(recipe_name,))
    res=cur.fetchone()
    if res:
        print("Recipe already in cookbook")
    else:
        cur.execute("INSERT INTO recipes VALUES (?,?,?)",(recipe_name,ingredients,instructions))
        for i in ingredients.split(','):
            cur.execute(""" INSERT OR IGNORE INTO ingredients VALUES(?,?) """,(i.strip(),False))
        con.commit() 
        print("Recipe succesfully added to cookbook") 
    return

def delete_recipe(con,cur):
    recipe_name=input("Which recipe would you like to delete? ")
    cur.execute
    res=cur.execute(""" DELETE
                        FROM recipes
                        WHERE name=?""",(recipe_name,))
    if res.rowcount>0:
        con.commit()
        print("Recipe sucessfully removed from cookbook")
    else:
        print("Recipe not in cookbook")
    return

def see_recipes(con,cur):
    cur.execute("""SELECT * FROM recipes""")
    res=cur.fetchall()
    if res:
        print("Recipes in cookbook: ")
        for i in res:
            print(i)
    else:
       print("No recipes in cookbook")
    return

def insert_ingredient(con,cur):
    ingr_name=input("What is the name of the ingredient? ") 
    cur.execute(""" SELECT *
                    FROM ingredients
                    WHERE name=?""",(ingr_name,))
    res=cur.fetchone()
    if res:
        print(res[1])
        if(res[1]):
            print("Ingredient already in cupboard")
        else:
            cur.execute("UPDATE ingredients SET is_in_cupboard=? WHERE name=?",(True,ingr_name))
            con.commit() 
            print("Ingredient succesfully added to cupboard")
    else:
        cur.execute("INSERT INTO ingredients VALUES (?,?)",(ingr_name,True))
        con.commit() 
        print("Ingredient succesfully added to cupboard")     
    return

def delete_ingredient(con,cur):
    ingr_name=input("Which ingredient would you like to delete? ")
    cur.execute(""" SELECT *
                    FROM ingredients
                    WHERE name=?""",(ingr_name,))
    res=cur.fetchone()
    if res:
        if(res[1]):
            cur.execute("UPDATE ingredients SET is_in_cupboard=? WHERE name=?",(False,ingr_name))
            con.commit()
            print("Ingredient sucessfully removed from cupboard") 
        else:
            print("Ingredient not in cupboard")
    else:
        print("Ingredient not in cupboard")
    return

def see_ingredients(con,cur):
    cur.execute("""SELECT * FROM ingredients WHERE is_in_cupboard""")
    res=cur.fetchall()
    if res:
        print("Ingredients in cupboard: ")
        for i in res:
            print(i[0])
    else:
       print("No ingredients in cupboard")
    return

def see_data(con,cur):
    cur.execute("""SELECT * FROM ingredients""")
    res=cur.fetchall()
    if res:
        print("Ingredients in database: ")
        for i in res:
            print(i)

def split_string(text,delimiter=','):
    return re.split(delimiter,text)

def create_split_function(con):
    con.create_function("split_string", 1, split_string)

def see_sugestions(con,cur):        # return recipes that have only ingredients on the cupboard
    create_split_function(con)
    query = """ 
                WITH cupboardIngredients AS (
                    SELECT name FROM ingredients WHERE is_in_cupboard
                )
                SELECT *
                FROM recipes r
                WHERE NOT EXISTS (
                    SELECT trim(value) AS ingredient
                    FROM (         
                        SELECT * 
                        FROM split_string(r.ingredients,','))
                    WHERE ingredient NOT IN cupboardIngredients         
                )          
            """  
    cur.execute(query)
    res=cur.fetchall()
    if res:
        print("Suggested recipes: ")
        for i in res:
            print(i)
    else:
        print("No recipes in cookbook with only available ingredients.")
    return




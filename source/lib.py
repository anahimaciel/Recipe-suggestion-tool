import sqlite3 as sq3 

def insert_recipe(con,cur):
    recipe_name=input("What is the name of the recipe? ")
    ingredients=input("What are the ingredients of the recipe? ")
    instructions=input("What are the instructions? ")
    cur.execute(""" SELECT name
                    FROM recipes
                    WHERE name=?""",(recipe_name,))
    res=cur.fetchone()
    if res:
        print("Recipe already in database")
    else:
        cur.execute("INSERT INTO recipes VALUES (?,?,?)",(recipe_name,ingredients,instructions))
        for i in ingredients.split(','):
            cur.execute(f""" if NOT EXISTS ( SELECT * from ingredients WHERE name = {i} )
                            INSERT INTO ingredients VALUES(?,?)""",(i,False))
        con.commit() 
        print("Recipe succesfully added to database") 
    return

def delete_recipe(con,cur):
    recipe_name=input("Which recipe would you like to delete? ")
    cur.execute
    res=cur.execute(""" DELETE
                        FROM recipes
                        WHERE name=?""",(recipe_name,))
    if res.rowcount>0:
        con.commit()
        print("Recipe sucessfully removed from database")
    else:
        print("Recipe not in database")
    return

def see_recipes(con,cur):
    cur.execute("""SELECT * FROM recipes""")
    res=cur.fetchall()
    if res:
        print("Recipes in database: ")
        for i in res:
            print(i)
    else:
       print("No recipes in database")
    return

def insert_ingredient(con,cur):
    ingr_name=input("What is the name of the ingredient? ") 
    cur.execute(""" SELECT name
                    FROM ingredients
                    WHERE name=?""",(ingr_name,))
    res=cur.fetchone()
    if res:
        if(res['is_in_cupboard']):
            print("Ingredient already in database")
        else:
            cur.execute("UPDATE ingredients SET is_in_cupboard=? WHERE name=?",(True,ingr_name))
            con.commit() 
            print("Ingredient succesfully added to database")
    else:
        cur.execute("INSERT INTO ingredients VALUES (?,?)",(ingr_name,True))
        con.commit() 
        print("Ingredient succesfully added to database")     
    return

def delete_ingredient(con,cur):
    ingr_name=input("Which ingredient would you like to delete? ")
    cur.execute
    res=cur.execute(""" DELETE
                        FROM ingredients
                        WHERE name=?""",(ingr_name,))
    if res.rowcount>0:
        con.commit()
        print("Ingredient sucessfully removed from database")
    else:
        print("Ingredient not in database")
    return

def see_ingredients(con,cur):
    cur.execute("""SELECT * FROM ingredients WHERE is_in_cupboard""")
    res=cur.fetchall()
    if res:
        print("Ingredients in database: ")
        for i in res:
            print(i)
    else:
       print("No ingredients in database")
    return

#def see_sugestions(con,cur):        # return recipes that have only ingredients on the cupboard
    #res=cur.execute("""SELECT name, ingredients 
    #            FROM recipes""")
    #for i in res:
    #    ingr_list=i[1].split(",")
    #    cur.execute(f"""SELECT name FROM ingredients WHERE name IN {ingr_list}""")
    #    for j in cur:
    #subquery returns lines with ingredients that arent on the cupboard
    #query=
    """         WITH cupboardIngredients AS (
                    SELECT 
                )
                SELECT name
                FROM recipes
                WHERE NOT EXISTS (          
                    SELECT 
                )
    """         
    #return





#Exercise 06 - A recipe

cookbook = {'sandwich' :
             {'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
              'meal' : 'lunch',
              'prep_time' : 10},
            'cake' :
             {'ingredients' : ['flour', 'sugar', 'eggs'],
              'meal' : 'dessert',
              'prep_time' : 60},
            'salad' :
             {'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
              'meal' : 'lunch',
              'prep_time' : 15},
           }


def func_opt_1(name, ingr, meal, time):    
    cookbook[name] = {'ingredients': ingr.split(', '),
                      'meal': meal,
                      'prep_time': time}    
    print(f"\nRecipe for {name} has been added.")

def func_opt_2(name):    
    cookbook.pop(name)
    print(f"\nRecipe for {name} has been deleted.")

def func_opt_3(name):    
    print((f"\nRecipe for {name}:\nIngredients list: " 
           f"{', '.join(cookbook[name]['ingredients'])}\n"
           f"To be eaten for {cookbook[name]['meal']}.\nTakes "
           f"{cookbook[name]['prep_time']} minutes of cooking."
         ))     

def func_opt_4():    
    for name, contents in cookbook.items():        
        print((
               f"\nRecipe for {str(name)}:"
               f"\nIngredients list: "
               f"{str(', '.join(contents['ingredients']))}"
               f"\nTo be eaten for {str(contents['meal'])}"
               f"\nTakes {int(contents['prep_time'])} minutes of cooking."
             ))
    
def func():

    menu = ("\nPlease select an option by typing the corresponding number:\n"
            "1: Add a recipe\n"
            "2: Delete a recipe\n"
            "3: Print a recipe\n"
            "4: Print the cookbook\n"
            "5: Quit\n")  

    opt_error = ("\nThis option does not exist, please type the corresponding "
                 "number.\nTo exit, enter 5.")

    recipe_error = "\nThere is no such recipe, please choose another."

    recipe_db = ', '.join(cookbook.keys())
    recipe_prompt = f"\nYou can choose among following receipts: {recipe_db}"
    
    print(menu)

    opt = input()

    try:
    
        if int(opt) == 1:            
            recipe_name = input(
                "\nPlease enter the name of the recipe you want to add: ")
            recipe_ingredients = input(
               "Please type in the ingredients, separating each one with a "
               "comma:\n")
            recipe_meal = input("Please enter the meal type: ")
            recipe_prep_time = int(input(
                "Please enter the preparation time: "))
            func_opt_1(
                recipe_name, recipe_ingredients, recipe_meal, recipe_prep_time)             
            func()
                
        elif int(opt) == 2:
            print(recipe_prompt)            
            delete_recipe = input(
                "\nPlease enter the recipe's name to delete it:\n")
            if delete_recipe in cookbook.keys():
                func_opt_2(delete_recipe)
            else:
                print(recipe_error)
            func()           

        elif int(opt) == 3:
            print(recipe_prompt)        
            prnt_recipe = input(
                "\nPlease enter the recipe's name to get its details:\n")
            if prnt_recipe in cookbook.keys():
                func_opt_3(prnt_recipe)               
            else:
                print(recipe_error)
            func()

        elif int(opt) == 4:
            func_opt_4()            
            func()
    
        elif int(opt) == 5:
            print("\nCookbook closed.")

        else:
            print(opt_error)
            func()

    except ValueError:
        print(opt_error)
        func()
        
func()


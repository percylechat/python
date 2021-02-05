"""
First, you will have to create a cookbook dictionary called cookbook.
cookbook will store 3 recipes:•sandwich•cake•saladEach recipe will store 3 values:
•ingredients: a list of ingredients
•meal: type of meal
•prep_time: preparation time in minutes
Sandwich's ingredients are ham, bread, cheese and tomatoes. It is a lunch and it takes 10minutes of preparation.
Cake's ingredients are flour, sugar and eggs. It is a dessert and it takes 60 minutes ofpreparation.
Salad's ingredients are avocado, arugula, tomatoes and spinach. It is a lunch and it takes15 minutes of preparation.

1. Get to know dictionaries. In the first place, try to print only the keys of the dictionary. Thenonly the values. 
And to conclude, all the items.
2. Write a function to print a recipe from cookbook. The function parameter will be: name ofthe recipe.
3. Write a function to delete a recipe from the dictionary. The function parameter will be: nameof the recipe.
4. Write a function to add a new recipe to cookbook with its ingredients, its meal type and itspreparation time. 
The function parameters will be: name of recipe, ingredients, meal andprep_time.
5. Write a function to print all recipe names from cookbook. Think about formatting theoutput.
6. Last but not least, make a program using the four functions you just created.

The program will prompt the user to make a choice between 
printing the cookbook
printingonly one recipe
adding a recipe
deleting a recipe
quitting the cookbook
"""

def add_recipe(r_name : str, r_ingr :str, r_prep_time : int, r_type : str):
    cookbook[r_name] = {}
    cookbook[r_name]['ingredients'] = r_ingr
    cookbook[r_name]['prep_time'] = r_prep_time
    cookbook[r_name]['type'] = r_type

def del_recipe(name : str):
    del cookbook[name]

def print_cookbook(cookbook):
    print(cookbook)

def print_recipe(r_name):
    if r_name in cookbook.keys():
        print(cookbook[r_name])
    else:
        print("Sorry, this recipe does not exist!")

cookbook = {}
cookbook['Cake'] = {'ingredients' : ('flour', 'sugar', 'egg'), 'prep_time' : 60, 'type' : 'dessert'}
cookbook['Salad'] = {'ingredients' : ('avocado', 'arugula', 'tomatoes', 'spinach'), 'prep_time' : 15, 'type' : 'lunch'}
cookbook['Sandwitch'] = {'ingredients' : ["ham", "bread", "cheese", "tomatoes"], 'prep_time' : 10, 'type' : 'lunch'}

def questions():
    while True:
        option : int = int(input("What do you want?\n1.Print the cookbook\n2.Print a recipe\n3.Add a recipe\n4.Delete a recipe\n"))
        if option == 1:
            print_cookbook(cookbook)
        if option == 2:
            r_name : str = input('Which recipe?\n')
            print_recipe(r_name)
        if option == 3:
            r_name : str = str(input('What is the name of the recipe?\n'))
            r_ingr = str(input('What are its ingredients?\n'))
            r_prep_time : int = int(input('How long does it take to cook it?\n'))
            r_type : str = str(input('What type of meal is it?\n'))
            add_recipe(r_name, r_ingr, r_prep_time, r_type)
        if option == 4:
            name : str = input('Which recipe?\n')
            del_recipe(name)

if __name__ == "__main__":
    questions()
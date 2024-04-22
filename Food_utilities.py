"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-03-10"
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    # Your code here
    # Enter the name
    name = input("Name: ")

    # Format the origin options in a new line
    print("Origin")
    print(Food.origins(), ':', end=' ')
    origin = int(input())

    # Checks if user enters Y or N for vegetarian input
    vegetarian_input = input("Vegetarian (Y/N): ").upper()
    is_vegetarian = True if vegetarian_input == "y" else False

    calories = int(input("Calories: "))

    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    # Your code here
    # Split the individual pieces of data based on vertical bar - delimitation
    data = line.split('|')

    # Extract the values from each row
    name = data[0]
    origin = int(data[1])
    is_vegetarian = data[2].lower() == "true"
    calories = int(data[3])

    # Create a Food object/instance using the extracted data
    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []
    # Your code here
    # Iterate through each line in the file
    for line in file_variable:
        # Create a food object from current line by using the read_food function
        food = read_food(line.strip())
        # Append the Food object to the foods list.
        foods.append(food)

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    for i in foods:
        food = f"{i.name}|{i.origin}|{i.is_vegetarian}|{i.calories}\n"
        file_variable.write(food)
    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    # Your code here

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    # Your code here
    origins = []

    for food in foods:
        if food.origin == origin:
            origins.append(food)
    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    total_calories = 0
    count = 0
    # Your code here
    for food in foods:
        total_calories += food.calories
        count += 1

    avg = total_calories/count
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    # Your code here

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    # Sort the foods list by name
    sorted_foods = sorted(foods, key=lambda x: x.name)

    # Creation of a country dictionary to identify the country the food originated from.
    countries_dict = {0: "Canadian", 1: "Chinese", 2: "Indian",
                      3: "Ethiopian", 4: "Mexican", 5: "Greek", 6: "Japanese",
                      7: "Italian", 8: "American", 9: "Scottish", 10: "New Zealand", 11: "English"}

    # Print the table header
    print("{:<40} {:<15} {:<15} {:<10}".format(
        "Name", "Origin", "Vegetarian", "Calories"))
    print("{:<40} {:<15} {:<15} {:<10}".format(
        "-" * 40, "-" * 15, "-" * 15, "-" * 10))

    # Print each food entry in the table
    for food in sorted_foods:
        print("{:<40} {:<15} {:<15} {:<10}".format(
            food.name, countries_dict.get(int(food.origin)), str(food.is_vegetarian), food.calories))

    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    # Your code here

    return result

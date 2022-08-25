colors_set = {"purple", "red", "blue", "orange", "yellow", "green"}

# Problem 1 (Sets)

"""
Create a new Set with string values that represent colors
Loop through the Set and print each value
"""


def print_colors(set_of_colors):
    for color in set_of_colors:
        print(color)

# print_colors(colors_set)

# Problem 2 (Sets)

"""
Take the Set from Problem 1
Take input from the user, asking for their favorite color
Check to see if their favorite color is in the Set
If the color is in the Set, print "We found your favorite color!"
If the color is not in the Set, add that color to the Set
"""


def find_favorite_color(set_of_colors):
    user_fav_color = input("What is your favorite color? ")
    if user_fav_color in set_of_colors:
        print("We found your favorite color!")
    else:
        set_of_colors.add(user_fav_color)
        print("Your favorite color has been added")

# find_favorite_color(colors_set)

# Problem 3 (Sets)
"""
Take the Set from Problem 1
Display the contents to the user in the terminal
Ask the user what colors they would like to add
Create a NEW Set with colors the user adds
Then utilize the `union` Set method to combine sets
display the new Set
See: https://www.w3schools.com/python/python_sets_join.asp
"""


def add_colors(set_of_colors):
    for color in set_of_colors:
        print(color)
    user_colors_str = input("What colors would you like to add? ")
    user_colors_list = user_colors_str.split()
    user_colors_set = set(user_colors_list)
    complete_color_set = set_of_colors.union(user_colors_set)
    for color in complete_color_set:
        print(color)

# add_colors(colors_set)

# Recommend having this resource open for Problems 4-6
# https://www.w3schools.com/python/python_tuples.asp

# Problem 4 (Tuples)

"""
Write a Tuple that contains strings that represent coins
There will be three types of coins: "gold", "silver", and "copper"
For example: ("gold", "silver", "copper", "gold")
Note that there are duplicates (imagine coins in a purse)
Next, write a function that displays all coins using a WHILE loop

"""

coins_tuple = ("gold", "silver", "copper", "gold", "silver", "silver", "copper")


def display_coins(coins):
    tuple_length = len(coins)
    counter = 0
    while counter < tuple_length:
        print(coins[counter])
        counter += 1

# display_coins(coins_tuple)


# Problem 5 (Tuples)

"""
Take the Tuple from Problem 4 and add a new coin to it
Then, display all of the coins in the Tuple after adding the coin
NOTE: You will need to convert your Tuple to a List, then back to a Tuple in order to do this!
See: https://www.w3schools.com/python/python_tuples_update.asp
"""


def add_coin(coins):
    coins_list = list(coins)
    coins_list.append("copper")
    coins = tuple(coins_list)
    tuple_length = len(coins)
    counter = 0
    while counter < tuple_length:
        print(coins[counter])
        counter += 1

# add_coin(coins_tuple)

# Problem 6 (Tuples)

"""
Take the Tuple from Problem 4 and remove all of the duplicates from it
Then, display all of the "coin types" to the user
Example Output: "gold, silver, copper"
NOTE: You will need to convert your Tuple to a Set, then back toa Tuple in order to de-duplicate
"""


def display_coin_types(coins):
    coins_set = set(coins)
    coins_type = tuple(coins_set)
    print("Coin Types")
    tuple_length = len(coins_type)
    counter = 0
    while counter < tuple_length:
        print(coins_type[counter])
        counter += 1

display_coin_types(coins_tuple)
# Problem 1

"""
Write a function that takes in a List and returns a List with the original list values reversed

Example Input: [1, 2, 3, 4, 5] 
Example Output: [5, 4, 3, 2, 1]
"""
number_list = [1,2, 3, 4, 5]

def reverse_list(list):
    # NOTE: This is not a completed problem!
    reversed_list = []
    for index in range (len(list) -1, -1, -1):
        reversed_list.append(list[index])
    return reversed_list

# print(reverse_list(number_list))

# Problem 2

"""
Write a function that has two parameters.
The first parameter will be a list of numbers, the second parameter will be a number.
Iterate over the list & compare each value to the number parameter
If it is greater than the number parameter, add it to a new list
Return the new list

Example Input: [1, 2, 3, 4, 5], 3 
Example Output: [4, 5]
"""


def list_value_checker(list, number):
    greater_numbers = []
    for index in range (len(list)):
        if number < list[index]:
            greater_numbers.append(list[index])
    return greater_numbers

# print(list_value_checker(number_list, 3))

# Problem 3

"""
Write a function that has two parameters: a list, and another list
Both lists that are passed in should contain the first names of people
Iterate over the lists comparing the values at each index from one list to the other. 
If there is a matching name in both lists, return that name from the function

Example Input: [“Nevin”, “David”, “Mike”], [“Brett”, “Mike”, “Dan"]
Example Output: "Mike"
"""

list_one = ["Brett", "Mike", "Dan"]
list_two = ["Nevin", "David", "Mike"]

def list_value_comparison(list_one, list_two):
    matching_values = []
    for index in range (len(list_one)):
        for i in range(len(list_two)):
            if list_one[index] == list_two[i]:
                matching_values.append(list_two[i])
    return matching_values

# print(list_value_comparison(list_one, list_two))
# Problem 4

"""
Write a function that takes in the following dictionary
and returns the value of the key "favorite_color"

person = {
    "name": "Timmy Thomas",
    "age": 5,
    "interests": {
        "favorite_book": "Where The Sidewalk Ends",
        "favorite_movie": "Star Wars",
        "favorite_color": "Red"
    }
}

Expected Output: "Red"
"""

person = {
    "name": "Timmy Thomas",
    "age": 5,
    "interests": {
        "favorite_book": "Where The Sidewalk Ends",
        "favorite_movie": "Star Wars",
        "favorite_color": "Red"
    }
}

def get_value_of_favorite_color(sample_dictionary):
    interests = sample_dictionary["interests"]
    fav_color = interests["favorite_color"]
    print(interests)
    return fav_color

# print(get_value_of_favorite_color(person))

# Problem 5


"""
Problem 4 - Write a function that takes in the following dictionary and prints out every
key and value in a well-formatted print statement

address = {
	"street": "123 Sesame Street",
	"city": "Some Town",
	"state": "Some State",
	"zip_code": 12345
}

Example Output
"street - 123 Sesame Street"
"city - Some Town"
"state - Some State"
"zip_code - 12345"

# BONUS: "clean" the key names so they print in a more readable format:
# Example: "Zip Code - 12345"
"""

address = {
	"street": "123 Sesame Street",
	"city": "Some Town",
	"state": "Some State",
	"zip_code": 12345
}

def dictionary_printer(dictionary):
    for item in dictionary:
        value = dictionary[item]
        pretty_key = item.title().replace("_", " ")         #can loop through and locate and change string instead for index in range(len(item)), ect
        print(f"{pretty_key} - {value}")

# dictionary_printer(address)

# Problem 6

"""
Write a function that takes in a List of numbers
Return a dictionary where the key is the number
And the value is how frequently it appears in the List


Example Input: [1, 1, 2, 2, 2, 3]
Example Output: {"1": 2, "2": 3, "3": 1}
"""
numbers_list = [1, 1, 2, 3, 4, 5, 5, 4, 6, 3]

def list_numbers_to_dictionary(list_of_numbers):
    numbers_dictionary = {}
    numbers_set = set(list_of_numbers)
    unique_numbers = list(numbers_set)
    for i in range (len(unique_numbers)):
        counter = 0
        for index in range (len(list_of_numbers)):
            if unique_numbers[i] == list_of_numbers[index]:
                counter += 1
        numbers_dictionary[unique_numbers[i]] = counter
    return numbers_dictionary

print(list_numbers_to_dictionary(numbers_list))
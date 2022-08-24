# List - ordered, changeable, allows duplicates
# Dictionary - ordered, changeable, unique keys-duplicate values
# Set - unordered, unchangeable, no duplicates
# Tuple - ordered, unchangeable, allows duplicates

my_numbers = [1, 2, 3, 1, 4, 2, 5, 6, 3, 4, 1, 5, 6, 8, 15, 12, 1,3, 5, 2, 6, 4, 7, 9, 12]
unique_numbers = set(my_numbers)
print(unique_numbers)
final_numbers = list(unique_numbers)
print(final_numbers)

fav_colors = ("blue", "teal", "green", "pink", "purple", "red")
list_colors = list(fav_colors)
print(list_colors)
list_colors[-1] = "sea-green"
fav_colors = tuple(list_colors)
print(fav_colors)
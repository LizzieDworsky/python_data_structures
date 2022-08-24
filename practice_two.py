
# Sets - unordered, unchageable, and no duplicates
my_foods = {"pancakes", "pizza", "curry", "tacos", "ice cream"}     # create set
for food in my_foods:       # iterate set
    print(food)
# membership test
has_pizza = "pizza" in my_foods
print(has_pizza)
has_eggs = "eggs" in my_foods
print(has_eggs)
my_foods.add("frosty")      # .add a single item
print(my_foods)
# .update iterable
more_foods = ["burger", "fries", "shake"]
my_foods.update(more_foods)
print(my_foods)
my_foods.remove("burger")   #throws error if item doesn't exist
my_foods.discard("shake")   #no error if item doesn't exist
print(my_foods)
            # get a random value from the set
# some_food = my_foods.pop()
# print(my_foods)
# print(some_food)
#             # .clear
# my_foods.clear()
# print(my_foods)

# Write a function with a Set

def food_checker(foods, food_to_find):
    if food_to_find in foods:
        print(f"{food_to_find} is here")
    else:
        print(f"{food_to_find} is not in this Set")

food_checker(my_foods, "pizza")
food_checker(my_foods, "hummus")

# Math Operations
david_foods = {"pizza", "lentil soup", "mac & cheese", "crab rangoon", "spinach mushroom lasagna"}
megan_foods = {"watermelon", "mac & cheese", "frosted animal crackers", "pad thai"}
amy_foods = {"pizza", "pad thai", "spaghetti squash", "tri-tip", "brownies", "mac & cheese"}
# union
my_union = david_foods.union(megan_foods, amy_foods)
print(my_union)
# intersection
my_intersection = david_foods.intersection(megan_foods, amy_foods)
print(my_intersection)
# isdisjoint
is_disjoint = david_foods.isdisjoint(megan_foods)
print(is_disjoint)
print(david_foods.isdisjoint(amy_foods))
# difference
my_difference = david_foods.difference(megan_foods, amy_foods)
print(my_difference)
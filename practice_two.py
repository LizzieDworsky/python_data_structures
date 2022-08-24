
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
some_food = my_foods.pop()
print(my_foods)
print(some_food)
# .clear
my_foods.clear()
print(my_foods)
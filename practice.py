#properties of data structures: chageability, orderability, and duplication
#data structure types list, dictionary, set, tuple

#sets
my_superpowers = {"flight", "invisibility", "super strength"}
print(my_superpowers)
my_empty_set = set()        #set constructor
print(my_empty_set)

for power in my_superpowers:
    print(power)
has_flight = "flight" in my_superpowers     #returns boolean value
print(has_flight)

some_other_powers = {"intellect", "super-speed"}
my_superpowers.add("laser eyes")
print(my_superpowers)
my_superpowers.update(some_other_powers)
print(my_superpowers)
even_more_powers = ["shrinking", "teleportation"]
my_superpowers.update(even_more_powers)
print(my_superpowers)

my_superpowers.remove("flight")
print(my_superpowers)
my_superpowers.discard("invisibility")
powers_count = len(my_superpowers)
print(f"There are {powers_count} powers in this set.")


#tuples
favorite_ice_creams = ("strawberry", "chocolate", "vanilla", "mint chocolate", "rasberry sorbet")
print(favorite_ice_creams)
best_ice_cream_shops = ("Brewsters",)
print(type(best_ice_cream_shops))
not_a_tuple = ("Missing a comma!")
print(not_a_tuple)

my_top_fav = favorite_ice_creams[4]
my_top_fav = favorite_ice_creams[-1]
top_three_favs = favorite_ice_creams[0:3]
print(my_top_fav)
print(top_three_favs)

more_flavors = ("coconut raisin", "lemon sorbet")
favorite_ice_creams += more_flavors
print(favorite_ice_creams)

print(more_flavors)
del more_flavors

flavor_count = len(favorite_ice_creams)
print(f"I have {flavor_count} flavors of ice cream.")


# data structure conversions
# tuple and set - unchangeable

my_unchangeable_tuple = ("red", "white", "green")
my_converted_tuple = list(my_unchangeable_tuple)
my_converted_tuple[0] = "blue"
my_unchangeable_tuple = tuple(my_converted_tuple)
print(my_unchangeable_tuple)

#sets don't allow duplicates
snack_favorties = ["banana", "popcorn", "popcorn", "candy bar", "veggies and hummus"]
remove_dupli_snacks = set(snack_favorties)
snack_favorties = list(remove_dupli_snacks)
# alternative
# snack_favorites = list(set(snack_favorties))
print(snack_favorties)
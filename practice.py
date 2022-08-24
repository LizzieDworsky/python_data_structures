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
print(f"I ahve {flavor_count} flavors of ice cream.")
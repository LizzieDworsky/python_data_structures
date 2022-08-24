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
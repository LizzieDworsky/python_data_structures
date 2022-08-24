#sets
my_superpowers = {"flight", "invisibility", "super strength"}
print(my_superpowers)
my_empty_set = set()        #set constructor
print(my_empty_set)

for power in my_superpowers:
    print(power)

has_flight = "flight" in my_superpowers     #returns boolean value
print(has_flight)
# Tuples - ordered, unchangeable, allows duplicates

destinations = ("New York City, USA", "Rome, Italy", "Paris, France", "Tokyo, Japan")

print(destinations[3])
print(destinations[-2])

non_usa_destinations = destinations[1:4]
print(non_usa_destinations)

has_paris = "Paris, France" in destinations
print(has_paris)
has_venice = "Venice, Italy" in destinations
print(has_venice)

more_destinations = ("Venice, Italy", "San Diego, USA", "Athens, Greece")
combined_destinations = more_destinations + destinations
print(combined_destinations)

# tuple unpacking
destination_one = destinations[0]
destination_two = destinations[1]
destination_three = destinations[2]
destination_four = destinations[3]
print(destination_one)
print(destination_two)
print(destination_three)
print(destination_four)
# vs
destination_one, destination_two, destination_three = more_destinations
print(destination_one)
print(destination_two)
print(destination_three)
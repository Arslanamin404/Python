s1 = {12, 5, 45, 12, 451, 2}
s2 = {5, 451, 425, 12, 2, 14}

print(f"Union: {s1.union(s2)}\n")
print(f"Intersection: {s1.intersection(s2)}\n")
s1.intersection_update(s2)
print(f"Intersection_Update: {s1}\n")
s1.update(s2)
print(f"Update adds the elements of 2 sets in 1: {s1}\n")

cities_1 = {"Srinagar", "Budgam", "Pulwama", "Tokyo"}
cities_2 = {"Budgam", "Pulwama", "Tokyo"}

# cities_1.intersection_update(cities_2)

print(f"Returns common values: {cities_1.intersection(cities_2)}\n")
print(f"Returns non common values: {cities_1.symmetric_difference(cities_2)}\n")

print(cities_1.difference(cities_2), "\n")

print(cities_1.issuperset(cities_2))

print(cities_1.issubset(cities_2))

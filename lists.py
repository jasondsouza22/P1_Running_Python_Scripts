# Declare a list variable
cities = ["Mumbai","Pune","Bangalore","Chennai"]

print(cities)
print(type(cities))
print(cities[1])

#append
cities.append("Nagpur")
cities.append(True)
cities.append(False)
print(cities)

#insert
cities.insert(3,"Delhi")
print(cities)

# Removing element from the end of the list
cities.pop()

# Removing element by using the index
cities.pop(3)
cities.pop()

print(cities)

for city in cities:
    print("The current value is:")
    print(city)

print("Process Completed")




Clubs = ["Manchester United", "Chelsea","Arsenal","Newcastle"]
for club in Clubs:
    print(club)


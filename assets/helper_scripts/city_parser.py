# used to parse incoming cities from array generated from grab_cities

arr = [] # this was the MASSIVE list of city names from grab_cities.js, just imagine theres strings here

firstChar = None
new_cities = []
for city in arr:
    if firstChar != city[0]:
        new_cities.append(city)
        firstChar = city[0]
        
new_cities = [(i, j)[1] for i, j in enumerate(new_cities) if i %4 ==0 ]
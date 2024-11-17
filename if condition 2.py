Countries ={"Australia" : ["Sydney","Melbourne","Brisbane","Perth"],
            "UAE" : ["Dubai","Abu Dhabi","Sharjah","Ajman"],
            "India" : ["Mumbai","Bangalore","Chennai","Delhi"]}
city = input("Enter a city name:").title()

for country, cities in Countries.items():
    if city  in cities:
        print(f"{city} is in {country}")
        print()

First_city = input("Enter the first city:").title()
Second_city = input("Enter the second city:").title()

country1 = Countries.get(First_city)
country2 = Countries.get(Second_city)

for country, cities in Countries.items():
    if First_city in cities:
        country1 = country
        break
for country,cities in Countries.items():
    if Second_city in cities:
        country2 = country
        break


if country1 and country1 == country2:
    print("Both cities are in",country1)
elif country1 and country2:
    print("They don't belong to the same country")
else:
    print("One or both cities not found in the list")


    
 

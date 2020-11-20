prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
city_list = []
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
        city_list.append(city)

print(f"The names of the cities visited are: \n {city_list}")
print(f"The last city visited is: {city_list[-1]}")

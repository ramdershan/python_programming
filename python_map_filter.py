menu = ['espresso', 'mocha', 'latte', 'cappuccino', 'cortado', 'americano']

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

# mapCoffee = map(find_coffee, menu)
# print(mapCoffee)
# for x in mapCoffee:
#     print(x)

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)
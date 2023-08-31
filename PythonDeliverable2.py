name = input("Welcome to the GC Fruit Market! What is your name?")
cart = []
total = 0
subtotal = 0
menu_options = {
    '1': "Grape 1$",
    '2': "Apple 2$",
    '3': "Orange 3$",
}


def print_menu():
    print('Welcome,' + name + '. What fruit would you like to buy?')
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


while True:

    print_menu()
    fruit = input()
    cart.append(int(fruit))
    answer = input('Would you like to buy another piece of fruit? y/n')
    if answer != 'y':
        break

for fruits in cart:
    print(fruits)
    subtotal += fruits

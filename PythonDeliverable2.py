name = input("Welcome to the GC Fruit Market! What is your name?")
cart = []
total = 0
subtotal = 0
apple = 0
grape = 0
orange = 0

menu_options = {
    1: " Grape 1$",
    2: " Apple 2$",
    3: " Orange 3$",
}


def print_menu():
    print('Welcome,' + name + '. What fruit would you like to buy?')
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


while True:

    print_menu()
    fruit = input()
    print('You bought 1'+ menu_options[int(fruit)])
    cart.append(int(fruit))
    answer = input('Would you like to buy another piece of fruit? y/n')
    if answer != 'y':
        break

for fruits in cart:
    if fruits == 1:
        grape += 1
    if fruits == 2:
        apple += 1
    if fruits == 3:
        orange += 1

print('Order for ' + name + ':')
print(str(grape) + ' Grape(s) at $1 apiece')
print(str(apple) + ' Apple(s) at $2 apiece')
print(str(orange) + ' Orange(s) at $3 apiece')

subtotal += fruits

    #count how
import numpy as np
import statistics


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
    print('Welcome,' + name + '. What fruit would you like to buy? ')
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


while True:

    print_menu()
    fruit = input()
    print('You bought 1'+ menu_options[int(fruit)][:-2] + 'at' + menu_options[int(fruit)][-3:])
    cart.append(int(fruit))
    answer = input('Would you like to buy another piece of fruit? y/n ')
    if answer != 'y':
        break

for fruits in cart:
    if fruits == 1:
        grape += 1
    if fruits == 2:
        apple += 1
    if fruits == 3:
        orange += 1
    subtotal += fruits

print('Order for ' + name + ':')
print(str(grape) + ' Grape(s) at $1 apiece')
print(str(apple) + ' Apple(s) at $2 apiece')
print(str(orange) + ' Orange(s) at $3 apiece')

total = subtotal * 1.05
tax = .05 * subtotal
print(f'Subtotal: ${sum(cart)}')
print('5% Tax: $', tax)
print("Total: $", total)
print(f'Median Price: ${np.median(cart)}')
print(f'Mode Price: ${statistics.mode(cart)}')

    #calculating subtotal and tax
    #printing receipt
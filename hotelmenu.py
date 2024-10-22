#Define menu of the restaurant
menu={
    'Pizza':40,
    'Pista':50,
    'Burger':60,
    'Salad':30,
    'Coffee':70
}
#Greet
print('Welcome to Python Restaurant')
print('Pizza: Rs40\nPista: Rs50\nBurger: Rs60\nSalad: Rs30\nCoffee: Rs70')

order_total=0

item_1 = input('Enter the name of item you want to order = ')
if item_1 in menu:
    order_total += menu[item_1]
    print(f'Your item {item_1} has been added to your order')
else:
    print(f'Ordered item {item_1} is not available yet!')

another_order=input('Do you want to add another item? (Yes/No)')
if another_order == 'Yes':
    item_2=input('Enter the name of second item= ')
    if item_2 in menu:
        order_total += menu[item_2]
        print(f'Ordered item {item_2} has been added to order')
    else:
        print(f'Ordered item {item_2} is not available yet!')

print(f'The total amount of items to pay is {order_total}')
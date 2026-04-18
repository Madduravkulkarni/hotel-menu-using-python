#defining the menu of Restaurant
menu={
    'pizza':100,
    'burger':70,
    'coffee':50,
    'maggie':55,
    'tea':20,
    'pasta':120,
    
}
#Greet
print('welcome to DEVINE Restaurant')
print("pizza:Rs100\nburger:Rs70\ncoffee:Rs50\nmaggie:Rs55\ntea:Rs20\npasta:Rs120\n")

order_total=0

item_1=input('enter the name of the item you want to order:')
if item_1 in menu:
    order_total=order_total+menu[item_1]
    print(f'your item {item_1} is added to your order')
else:
    print(f'your ordered item {item_1} not in the menu!')

another_item=input("do you want to add another item? (Yes/No)")
if another_item == 'Yes':
    item_2=input("enter the name of second item:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f'item {item_2} has been added to order')
    else:
        print(f'ordered item {item_2} is not available!')
another_item=input("do you want to add another item? (Yes/No)")
if another_item == 'Yes':
    item_3=input("enter the name of second item:")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f'item {item_3} has been added to order')
    else:
        print(f'ordered item {item_3} is not available!')


print(f'the total amount of items to pay is {order_total}')


####OUTPUT######
welcome to DEVINE restro
pizza:Rs100
burger:Rs70
coffee:Rs50
maggie:Rs55
tea:Rs20
pasta:Rs120

enter the name of the item you want to order:burger
your item burger is added to your order
do you want to add another item? (Yes/No)Yes
enter the name of second item:pasta
item pasta has been added to order
do you want to add another item? (Yes/No)Yes
enter the name of second item:coffee
item coffee has been added to order
the total amount of items to pay is 240







 

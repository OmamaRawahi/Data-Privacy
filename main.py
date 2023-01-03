
import datetime

order = 1
while True:
    print('  Welcome to GUtech Restaurant')
    print('Menu:')
    print("   1. Fries      R.O. 1.000")
    print("   2. Rice       R.O. 1.000")
    print("   3. Drinks     R.O. 1.000")
    print("   4. Pasta      R.O. 1.000")
    print("   5. Pizza      R.O. 1.000")

    print('Please select a transaction')
    print(' a. Make an order')
    print(' b. Exit')

    while True:
        x = input()

        if x == 'b':
            exit()
        elif x == 'a':
            break
        else:
            print("Invalid input, please enter 'a' or 'b'.")

    while True:
        table_number = input('Enter Table Number: ')
        try:
            table_number = int(table_number)
        except:
            table_number = -1
        if table_number > 0:
            break

    while True:
        number_guests = input('Enter Number of Guests: ')
        try:
            number_guests = int(number_guests)
        except:
            number_guests = -1
        if number_guests > 0:
            break

    menu = ['Fries', 'Rice', 'Drinks', 'Pasta', 'Pizza']
    prices = [1, 1.5, 0.5, 1.5, 2]

    orders = []
    print('Enter orders (press x to finish):')
    while True:
        x = input()

        if x == 'x':
            break
        elif '1' <= x <= '5':
            orders.append(x)
        else:
            print('Invalid input,try again')

    while True:
        tip = input('Enter Tip: ')
        try:
            tip = float(tip)
        except:
            tip = -1


        if tip >= 0:
             now = datetime.datetime.now()
             print()
             print()
             print(' GUtech Resturant')
             print()
             print(now.strftime('%d/%m/%y %H:%M'))
             print('Order No.', order)
             print('Table Number:', table_number)
             print('Order:')
             break
        else:
            print("Invalid input, please enter a valid tip amount")

    totalOrder = 0
    for i in orders:
        print(menu[int(i) - 1], ' ' * (10 - len(menu[int(i) - 1])) ,'R.O {:.3f}'.format(prices[int(i) - 1]))
    print("_" * 23)

    Tax = totalOrder * (5 / 100)
    total = totalOrder + Tax + tip
    print('Tax        ', 'R.O. {:.3f}'.format(Tax))
    print('Tips       ', 'R.O. {:.3f}'.format(tip))
    print('Total      ', 'R.O. {:.3f}'.format(total))

    while True:
        x = input('Do you want to split the price with guests? (Y/N) ')
        if x == 'Y':
            print(total/number_guests)
            break
        elif x == 'N':
            print(total)
            break
        else:
            print("Invalid input, try again.")

    order += 1
    print()
    print()

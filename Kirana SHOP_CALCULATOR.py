
print("Press 'q' if you want to exit")
a= 0

while True:
    User_input = input("Enter Price: ")
    # li.append(User_input)
    if User_input!= 'q':
        a = a+ int (User_input)
        print("Your bill total is =", a)
    else:
        print(f'Your total bill total is {a}')
        print("------------------------Thanks For shopping with us----------------------")






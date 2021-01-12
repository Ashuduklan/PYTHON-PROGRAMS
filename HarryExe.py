def Count_year(a, c):
    age = 2021 - a
    rem = 100 - age
    total  = 2021 + rem
    des = c - a
    print("You will achieve your century in: ",total)
    print("Your age in",c,"is: ",des)

def Count_age(b, d):
    remain = 100 - b
    achieve = 2021+remain
    des_age = b +(d-2021)
    print("You will get your Century in: ",achieve)
    print("Your age in",d,"is: ", des_age)


user_input = int(input("Your Age or Year of birth: "))
if 100>user_input>=1:
    desired_year = int(input("How old are you in desired year Enter year: "))
    Count_age(user_input, desired_year)

elif 150>user_input>100:
    print("You are oldest person alive...")

elif 1950<user_input<2021:
    desired_inp = int(input("How old are you in desired year Enter year: "))
    Count_year(user_input, desired_inp)
else:
    print("Please enter a correct Age or Year of birth!!!")





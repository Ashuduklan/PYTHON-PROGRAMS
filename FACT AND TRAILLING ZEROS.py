# tarilling zeros in factorial

def factorial(n):
    if n<=1:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact*i
        return fact
num = int (input("Enter the number: "))
a = factorial(num)
print("Fcatorial is =", a)
typ = str(a)
count = 0
for item in typ:
    if item=='0':
        count = count+1
print("No. of zero in Factorial: ",count)

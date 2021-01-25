# N =  input("Enter your string: ")


# for i in range(0, len(N)):
#     # print(N[i])
#     for j in range(0, i+1):
#         print(N[j], end=" ")
#     print()

# substring program
def Substr(str, n):
    for i in range(n):
        for j in range(i+1, n+1):
            print(str[i:j])

str = "Ashish"
n = len(str)
Substr(str, n)
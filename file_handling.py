# file = open('../week4/myPython.txt', 'r')

# print(file.read())

# try: 
#     file = open('../week4/myPython.txt', 'r')
#     print(file.read())
# except FileNotFoundError: 
#     print("File Not Found")
# finally :
#     print("This is the best you have done")

# Question 2

a = 5
b = 7

print(a*b)

try: 
    print(a*b)
    k = input("Enter a number:")
except :
    print("You cant multiply this with zero")
finally:
    print("Thank you for calculating with me")


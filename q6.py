# 6. Write a python script which takes a three digit number from the user and displays
# only its middle digit.

b=int(input("Enter a 3 digit number: "))

a=b//10
print("Middle digit of number",b,"is",a%10)

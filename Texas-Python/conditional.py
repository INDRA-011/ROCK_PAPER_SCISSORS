
'''
marks = int(input("enter Marks: "))

if marks >= 80:
    print("Congrats you have achieved Distinction")
elif marks >= 70:
    print("congrats you have achieved First Division")
elif marks >= 60:
    print("congrats you have achieved Second Division")
elif marks >= 40:
    print("Good Lad! you have Passed")
else: 
    print("you son of a gun, try again")


num1 = int(input("enter first num: "))
num2 = int(input("enter second num: "))

if num1 > num2:
    print(f"First number is greater: {num1} > {num2}")
elif num1 == num2:
    print(f"Number are Equal: {num2} == {num1}")
else: 
    print(f"Second number is greater: {num2} > {num1}")


#nested statement
age = int(input("Enter your age: "))


if age >= 16:
    voter_id = input("Do you have Voter ID: y/n. ")
    if voter_id == "y":
        print(f"Your age is {age}. Your are a Voter")
    else:
        print(f"Your age is {age}. But you need a Voter ID")
else:
    print(f"Your age is {age}. Not a valid Age")


num = int(input("enter any number: "))

if num % 2 == 0:
    print(f"The number {num} is Even")
else: 
    print(f"The number {num} is Odd")
'''

password = "123"
userinput = input("Enter the Pass: ")

if password == userinput:
    print(f"Your are Logged In.")
else:
    print(f"Login Rejected: Correct password: {password}")
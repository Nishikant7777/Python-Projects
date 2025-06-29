import random

num1=int(input("Enter the Number:"))  # user input for first digit

# operator=input("Enter the Operator:") # user input for the opration to be executed

operator=random.choice(['+','-','*','/']) # it gives random operators to perform the operations on the given numbers

num2=int(input("Enter the Number:"))  # user input for the second digit

if operator =='+':
    print("Result:->  " + str(num1+num2))

elif operator =='-':
    print("Result:->  " + str(num1-num2))

elif operator =='*':
    print("Result:->  " + str(num1*num2))

elif operator =='/':
    print("Result:->  " + str(num1/num2))

else :
    print("ERROR ::::ENTER THE DETAILS PROPERLY")


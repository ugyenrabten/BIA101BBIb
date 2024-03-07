# objective
# creata a program that in user input
# and determines the if the number is positive or negative
# print "your number is positive or negative or zero"
# if eles
# print()
# input)
# 1-3mins

# break down the problem
# 1: Take in user input
   # check the type of the input
# 2: check if the number is positive or negative or zero
   # need to use if else statement
   # you will be comparing numbers and not strings
# 3: Print the result

# 1: get user input
userInput = input('Please type any number: ')
userInputType = type(userInput)
print('The type of user input is:', userInputType)

userInputNumber = float(userInput)
print('The type of userInputNumber is:', type(userInputNumber))

# 2,3 - if else statement and print
if userInputNumber > 0:
    print('The number is positive')

elif userInputNumber < 0:
    print('The number is negative')

elif userInputNumber == 0:
    print('The number is zero')
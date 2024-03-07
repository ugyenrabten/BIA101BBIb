# ! check if user can vote

# ?Get user age from input
# ?convert userinput(str) to int() to number
# ?check if user can vote
    # ?if else statement
    # ?if above 18, print "You can vote"
    # ?if below 18, print "You canot vote"

userInput = input('Enter your age:')
userage = int(userInput)
if userage >= 18:
    print ('You can vote')
elif userage < 18:
    print ("You can't vote") 
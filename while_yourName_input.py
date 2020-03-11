#This is called input validation
#program keeps asking for user input until the user enters something valid
#you don't want the user entering 'tom' when you ask for their age or '48' for their name

name = ''
while name != 'your name':  #this loop will keep repeating until you type in the string "your name" w/o quotes
    print('Please type your name.')
    name = input()
print('Thank you!')


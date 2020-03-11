#this is similar the first yourName program, except it uses a break to end the program
#break statements are useful if you have several different places in a while loop that would allow you to leave from that point


name = ''
while True:  #this would never be False so it's an infinite loop because it's always True
    print('Please type your name.')
    name = input()
    if name == 'your name':  #uses an if statement to cause a break in the program so it doesn' run forever
        break
print('Thank you!')

#how to write your own functions
#functions help with grouping code that is run often or multiple times
#you can just call a function instead of writing the code each time
#always avoid duplicating code
#you can just change the function code and it changes everywhere the function is called


def hello(): #def statement defines the new function
#the code below is called the body of the function
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

#this calls the hello function 3 times
hello()
hello()
hello()

#this is a new function
def hello(name): #this function has a variable or parameter called 'name'
    print('Hello ' + name)

hello('Alice')
hello('Bob')


#can also get the parameters from user input

#can't get the input inside of the function???
def helloAgain(firstName):
    #firstName = input('What is your name?') WHY DOESN'T THIS WORK?
    print('Hello ' + firstName)

#you have to get the input when as a parameter when you call the function?
helloAgain(firstName=input('What is your name?'))

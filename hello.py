#this program says hello and asks for my name

print('Hello World!')

print('What is your name?') # ask for their name
myName = input() #assigns the user input to above question to the variable 'myName'
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName)) #prints the length (using the 'len' function of the name stored in the variable 'myName'

print('What is your age?') #ask for their age
myAge = input() #assigns the user input to the above question to the variable 'myAge'
print('You will be ' + str(int(myAge) + 1) + ' in a year.') #converts the integer 'myAge + 1' into a string so you can concatenate it with the other strings in the expression


#below shows ways to change the data types of values

#the 'input()' function always returns a string value, but you can convert it to an integer or float
#you can't concatenate an integer with a string so first convert the integer to string, then you can concatenate
str(26) #will return convert the integer, 26, to a string
int ('1234') #will convert the string, '1234', into an integer

#using float is useful if you are working with fractions or decimals
#if you don't want your calculations be rounded up or down
float('3.14') #converts the string, '3.14' to a float (decimal)
float(1) #coverts an integer, 1, to a float (decimal)

#similar to if_else statement, except this has multiple else statements

name = 'Bob'
age = 3000
if name == 'Alice': #this is false so it is skipped
    print('Hi Alice.')
elif age < 12:  #this is false so it is skipped
    print('You are not Alice, kiddo.')
elif age > 2000:  #this is true so it goes runs the code in this block
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:  #this is skipped because the previous statement was true
    print('You are not Alice, grannie.')

#the third elif statement is also true, but it stops running code
#after it reaches the first elif statement that is true and then skips
#the remaining elif blocks.

#THEREFORE, THE ORDER OF THE ELIF STATEMENTS IS VERY IMPORTANT!!

#you can also add an else statement at the end of the elif statements
#the else statement will only run if ALL of the elif statements are false
    
#Truthy and Falsey conditions
#the values 0, 0.0, and the empty string, '', are considered to be Falsey values.
#everything else is Truthey
#you can say use this to check if user has input something that is required
    #or if they just entered nothing (an empty string)
    #or if the value of something is 0

#can see which values are Truthey or Falsey by using the 'bool()' function
    #bool(0) would be false
    #bool('') would be false
    #bool(21) would be true
    #bool('Hello') would be true

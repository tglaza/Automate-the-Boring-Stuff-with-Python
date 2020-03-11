#continue statements are also used inside while loops

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:  #if this is true, go back to the start of the while loop (don't print 'spam is 3')
        continue  #this is what makes the program go directly back to the start of the while loop
    print('spam is ' + str(spam))  #have to convert the spam integer to a string before you can use string concatenation

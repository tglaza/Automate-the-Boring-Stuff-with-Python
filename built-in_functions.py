#python has built-in packages that have functions contained in them
#can import modules to get access to new functions
#the modules that come with Python are called the standard library
#can also install third-party modules using the pip tool (can't install it at work...no access error)

#first, have to import the package
import random   #this packages contains some functions (how can I find which functions are in a package?)
random.randint(1,10)    #use'packageName.functionName()' to use the function

#can import multiple packages at the same time by separating the package names with commas
import random, sys, os, math

#this is another way to import a package, but the import way is more clear when reading the code
from random import *    #this imports all functions contained in the 'random' package
randint(1,10)

#sometimes you want to end the program before it's done
import sys  #this package contains the 'exit' function
sys.exit()  #this function immediately ends the program

#install piperclip, part of the 'pip.exe' package so you can copy and paste using the clipboard
#need to run this from the command line, not as part of your python code file
#use the code below without the '#'
    #pip.exe install pyperclip

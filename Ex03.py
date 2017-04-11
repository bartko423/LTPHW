a = '109099' 
print a [0]
print a[0:5]


"""This lines will ask user and the it will Paraphrases his words 
using Strings after Print command using %s marks from brackets in showed order"""
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)


#It can be used when user will ask for date or hour info
#Fist it will import date module
from datetime import datetime

now = datetime.now() 
print now
print now.year
print now.month
print now.day


#this is Choose game
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()



#this is Decission game
def clinic():
    print ("You've just Woke in the clinic from the coma!\n\tEvrything is burnig you had to be quick")
    print "You saw 2 doors and window"
    print "Do you take the door on the left or the right or jump through the window?"
    answer = raw_input("Type left or right or straight and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    elif answer == "jump" or answer == "j":
        print "You landing at the the pawement and you sprains your's ankle"
    else:
        print "That wasn't smart! Try again."
	print
   pyt     "From the distance you can hear barking dogs and shouting men"
	print "This is chaos!!! You think"
        
        clinic()
clinic()

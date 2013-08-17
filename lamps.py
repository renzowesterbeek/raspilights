#!/usr/bin/python -tt
# Home automation lamps        #
#                              #
# Python version 2.7           #
# By Renzo Westerbeek (c) 2013 #

# Dictionary of lamps #
lamps = {
    "woon" : 0,
    "keuken" : 0
}

#####
######################
#####

# Function that prints out all items in dic "lamps" #
def printOut():
    print "Your lamps (" + str(len(lamps)) + "):"
    for items in lamps:
        print items
    print ""

# Turns lamp on or off #
def switch(status, lamp):
    if status == "on":
        #choose lamp on
        lamps[lamp] = 1;
        print ""
        print "Lamp " + lamp + " on"
        print ""
    else:
        #choose lamp off
        lamps[lamp] = 0;
        print ""
        print "Lamp " + lamp + " off"
        print ""
        
# Chooses what to do #
def chooseFunction():
    # Checks input of user
    choice = raw_input("Add, del or change a lamp?")
    choice = choice.lower()
    
    # Converts input of user
    if choice == "add":
        addLamp()
    elif choice == "del":
        deleteLamp()
    else:
        # Changes status of lamp
        settingsLamp()

# Asks for user input #
def settingsLamp():
    print "Change your settings:"
    lamp = raw_input("lamp: ")
    status = raw_input("on/off: ")
    switch(status, lamp)

def deleteLamp():
	print "Wich lamp to delete? "
	# lamp = raw_input("lamp: ")

def addLamp():
	print "Wich lamp do you want to add? "
	# lamp = raw_input("lamp: ")

# Displays status of lamps #
def printStatus():
    print "Status of lamps: "
    for items in lamps:
        if lamps[items] == 0:
            print items + ": off"
        else:
            print items + ": on"
    
#####
######################
#####

# Calls printOut function #
printOut()

# Calls chooseFunction function #
chooseFunction()

# Calls function that displays status of lamps #
printStatus()
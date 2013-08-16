#!/usr/bin/python -tt
# Home automation lamps        #
#                              #
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
    print "Your lamps (%d):" %
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
        print "Adds lamp"
    elif choice == "del":
        print "Deletes lamp"
    else:
        # Changes status of lamp
        changeSettings()

# Asks for user input #
def changeSettings():
    print "Change your settings:"
    lamp = raw_input("lamp: ")
    status = raw_input("on/off: ")
    switch(status, lamp)

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
from pyscript import document  # webpage module links
# your roll_dice function should be saved in a file named 'dice.py'
# uncomment the next line when you have this prepared
import dice


# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = "Coin"
#x = dice_type

def select_face_option(event): #used when you select dice type
    global dice_type  # use global var named dice_type
    
    x = document.getElementbyId("dice").value 
    #document.getElementbyId("dice").value - store as a variable and then store that value in dice_type
    #run if function
    #if(dice_type = 2)


def roll_all_dice(event): #called when you press the sbmit button
    global dice_type  # use global var named dice_type

#add function to figure out output

    #output = "???"
    #document.querySelector("div#roll-history").innerHTML = output

def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").innerHTML = ""  #DOM

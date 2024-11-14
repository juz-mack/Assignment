from pyscript import document  # webpage module links
# your roll_dice function should be saved in a file named 'dice.py'
# uncomment the next line when you have this prepared
import dice


# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = "Coin"
#roll_dice(sides) = dice_num

def select_face_option(event): #used when you select dice type
    global dice_type  # use global var named dice_type
    #global roll_dice(sides)

    dice_type = document.getElementById("dice").value
    if dice_type == "Coin":
        dice_num = 2
    elif dice_type == "d6":
        dice_num = 6
    elif dice_type == "d8":
        dice_num = 8
    elif dice_type == "d10":
        dice_num = 10
    elif dice_type == "d20":
        dice_num = 20
    elif dice_type == "d100":
        dice_num = 100

    roll_num = document.getElementById("num_roll").innerHTML

    #run "dice"


def roll_all_dice(event): #called when you press the submit button
    global dice_type  # use global var named dice_type
    #get roll count from input box
    ...

#add function to figure out output

    #for function?

    #output = "???"
    #document.querySelector("div#roll-history").innerHTML = output

def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").innerHTML = ""  #DOM

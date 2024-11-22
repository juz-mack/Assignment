from pyscript import document  # webpage module links
# your roll_dice function should be saved in a file named 'dice.py'
# uncomment the next line when you have this prepared
import dice

# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
# this section seems wrong?
dice_type = int("Coin")
roll_num = int(1)



def select_face_option(event): #used when you select dice type
    global dice_type  # use global var named dice_type
    global roll_num



    dice_type = document.getElementById("dice").value
    if dice_type == "Coin":
        value = 2
    elif dice_type == "d6":
        value = 6
    elif dice_type == "d8":
        value = 8
    elif dice_type == "d10":
        value = 10
    elif dice_type == "d20":
        value = 20
    elif dice_type == "d100":
        value = 100

    roll_num = document.getElementById("num_roll").value

    #run "dice"


def roll_all_dice(event): #called when you press the submit button
    global dice_type  # use global var named dice_type
    global roll_num
    sides = dice_type
    #get roll count from input box
    dice.roll_dice(sides)

    ...

#add function to figure out output


    #for function?

    output = "num"
    document.querySelector("div#roll-history").innerHTML = output

    #print(output)

def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").innerHTML = ""  #DOM

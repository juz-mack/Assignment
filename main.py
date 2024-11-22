from pyscript import document  # webpage module links
# your roll_dice function should be saved in a file named 'dice.py'
# uncomment the next line when you have this prepared
import dice

# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = 2



def select_face_option(event): #used when you select dice type
    global dice_type  # use global var named dice_type
    value = document.getElementById("dice").value
    if value == "Coin":
        dice_type = 2
    elif value == "d6":
        dice_type = 6
    elif value == "d8":
        dice_type = 8
    elif value == "d10":
        dice_type = 10
    elif value == "d20":
        dice_type = 20
    elif value == "d100":
        dice_type = 100


def roll_all_dice(event): #called when you press the submit button
    global dice_type  # use global var named dice_type
    num_roll = int(document.getElementById("num_roll").value)
    output = "Roll Results: "

    for roll_number in range(num_roll):
        roll_result = dice.roll_dice(dice_type)
        seperator = ", "
        print(roll_number)
        print(num_roll)
        if roll_result == num_roll:
            seperator = ""
        output = output + str(roll_result) + seperator
        print(output)

    document.querySelector("div#roll-history").innerHTML = output

def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").innerHTML = ""  #DOM

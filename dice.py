# put your dice_roll() function in this file

# using the 2 codes todgether - argv in command line and input function
# allows you to use as input funtion or via command line
import sys
import random as rnd

def get_numbers_argv():
    first_num = int(sys.argv[1])  #this will be dice type, d2,d6 etc
    second_num = int(sys.argv[2]) #this will change to number of dice to roll
    return (first_num,second_num)

def get_numbers_input():
    first_num = int(input("Number of sides > "))  #dice type, d2,d6 etc
    second_num = int(input("Number of rolls > ")) #change to number of dice to roll
    return (first_num,second_num)

def roll_dice(sides):
    num = rnd.randint(1, sides)
    return num

running = True
while running:              
    if len(sys.argv) > 1:  # this is len() asking if there are > 1 arguments in command line, if yes then == get_numbers_argv()
        numbers = get_numbers_argv()
    else:
        numbers = get_numbers_input()  #if no press enter then follow get_numbers_input()

    for roll in range(int(numbers[1])):   #careful of indents, top down then follows above if, then else, then below for, then keep_going loop at bottom
        result_d = roll_dice(int(numbers[0]))

        d_str = str(result_d)

        print("D" + str(numbers[0]), ": ", d_str)

    keep_going = input("Roll again (Y/N) ? ")
    if keep_going != 'Y' and keep_going != 'y' :
        running = False
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroad = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right' ")
if crossroad == 'left':
    lake = input("You arrived at a lake. Do you wish to wait for a boat or swim across? Type 'wait' or 'swim' ")
    if lake == 'wait':
        door = input("You arrived on the final island. Choose between the three doors to find your treasure! Type 'yellow', 'red' or 'blue' ")
        if door == 'yellow':
            print("You found the treasure. You won!")
        elif door == 'red':
            print("You fell into a fire. Game over!")
        elif door == 'blue':
            print("You fell back into the lake, crocodiles have surrounded you. Game over!")
    else:
        print("You are surrounded by Crocodiles. Game over!")
else:
    print("You fell into a hole. Game over!")


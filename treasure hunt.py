import random

def intro():
    print("Welcome to the Treasure Hunt Game!")
    print("You are an adventurer seeking a hidden treasure.")
    print("Your journey begins now!\n")

def first_choice():
    print("You find yourself at the entrance of a dark cave. Two paths lie before you:")
    print("1. Enter the cave.")
    print("2. Walk around the cave.")
    
    choice = input("What do you choose? (1/2): ")
    if choice == '1':
        enter_cave()
    elif choice == '2':
        walk_around_cave()
    else:
        print("Invalid choice! Please enter 1 or 2.")
        first_choice()

def enter_cave():
    print("\nYou bravely enter the cave...")
    print("As you venture deeper, you hear a noise.")
    print("You have two options:")
    print("1. Investigate the noise.")
    print("2. Keep moving quietly.")
    
    choice = input("What do you choose? (1/2): ")
    if choice == '1':
        investigate_noise()
    elif choice == '2':
        move_quietly()
    else:
        print("Invalid choice! Please enter 1 or 2.")
        enter_cave()

def investigate_noise():
    print("\nYou decide to investigate the noise...")
    outcome = random.choice(['treasure', 'trap', 'nothing'])
    if outcome == 'treasure':
        print("Congratulations! You found the hidden treasure behind a rock!")
    elif outcome == 'trap':
        print("Oh no! It's a trap! You fell into a pit!")
        game_over()
    else:
        print("It was just a rat. You continue your journey.")
        enter_cave()

def move_quietly():
    print("\nYou move quietly through the cave...")
    outcome = random.choice(['treasure', 'nothing'])
    if outcome == 'treasure':
        print("You found the hidden treasure deep inside the cave! Well done!")
    else:
        print("There was nothing of interest, but you safely exit the cave.")
        print("Unfortunately, no treasure was found this time.")
    
def walk_around_cave():
    print("\nYou decide to walk around the cave...")
    print("Suddenly, you encounter a river.")
    print("You can either:")
    print("1. Build a raft and cross the river.")
    print("2. Look for a bridge upstream.")
    
    choice = input("What do you choose? (1/2): ")
    if choice == '1':
        cross_river_raft()
    elif choice == '2':
        find_bridge()
    else:
        print("Invalid choice! Please enter 1 or 2.")
        walk_around_cave()

def cross_river_raft():
    print("\nYou start building a raft...")
    outcome = random.choice(['safe_crossing', 'raft_sinks'])
    if outcome == 'safe_crossing':
        print("You successfully crossed the river and found the treasure on the other side!")
    else:
        print("The raft sinks halfway across the river. You swim back to shore. No treasure this time.")
        game_over()

def find_bridge():
    print("\nYou decide to search for a bridge upstream...")
    print("After hours of walking, you finally find one!")
    print("But unfortunately, there's no treasure on the other side.")
    game_over()

def game_over():
    print("\nGame Over! Better luck next time.")
    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() == 'yes':
        first_choice()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    intro()
    first_choice()

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of a closed door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if "honey" in choice:
        # if choice == "take honey":
            dead("The bear eats your face off.")
        elif "taunt" in choice and not bear_moved:
        # elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can open it it now.")
            bear_moved = True
        elif "taunt" in choice and bear_moved:
        # elif choice == "taunt bear" and bear_moved:
            dead("The bear eats your legs.")
        elif "open door" in choice and bear_moved:
        # elif choice == "open door" and bear_moved:
            gold_room()
        else:
            # print("I got no idea what this means.")
            dead("TOO LATE, BEAR ATTACKS.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()

# GAME for some reason.
from sys import exit
import random

# punches = ['left', 'right', 'uppercut']

def fight():
    print("Would you like to start a boxing match?")

    choice = input("> ")

    if choice == "yes":
        start()
    elif choice == "no":
        exit(0)
    else:
        print("yes or no please.")
        fight()

def start():
    hits = 0
    counter_hit = 0

    print("Ready to fight? dodge left or dodge right")
    print("Ding Ding!")

    print("Your opponent threw a left hook!")

    choice = input("> ")

    if "dodge left" in choice:
        print("You dodged and landed a hit!")
        counter_hit += 1
    else:
        print("Too slow!")
        hits += 1

    print(f"{hits} hits so far!")
    print(f"{counter_hit} counters so far!")


    print("Your opponent threw a right hook!")

    choice = input("> ")

    if "dodge right" in choice:
        print("You dodged and landed a hit!")
        counter_hit += 1
    else:
        print("Too slow!")
        hits += 1

    print(f"{hits} hits so far!")
    print(f"{counter_hit} counters so far!")

    print("Your opponent threw a right hook!")

    choice = input("> ")

    if "dodge right" in choice:
        print("You dodged and landed a hit!")
        counter_hit += 1
    else:
        print("Too slow!")
        hits += 1

    print(f"{hits} hits so far!")
    print(f"{counter_hit} counters so far!")

    if hits < counter_hit:
        print("You win!")
        exit(0)
    # elif hits == 3:
    #     print("You got knocked out!")
    #     exit(0)
    # elif counter_hit == 3:
    #     print("You knocked them out!")
    #     exit(0)
    else:
        print("You lose!")
        exit(0)

fight()

from sys import exit

def gold_room():
    print("This room is full of god. How much do you take? ")

    choice= input("> ")


    if "0" in choice or "1" in choice:
        how_much=int(choice)
    elif choice=="Help":
        print("Enter a number of the amount of Gold you wish to take.")
    else:
        dead("Man, learn to type a number.")

    if how_much<50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy Bastard!")


def bear_room():
    print("There is a bear here. ")
    print("The bear has a bunch of honey. ")
    print("The fat bear is infront of another door. ")
    print("How are you going to move the bear? ")
    bear_moved= False

    while True:
        choice=input("> ")

        if choice=="Take honey":
            dead("The bear looks at you and slaps your face off. ")
        elif choice=="Take bear" and not bear_moved:
            dead("The bear gets pissed off and chews your leg off. ")
        elif choice=="Taunt bear" and not bear_moved:
            print("The bear has moved from the door. ")
            print("You can go through it now.")
            bear_moved=True
        elif choice=="What do I do now?":
                print("open door, dumbass.")
        elif choice=="open door" and bear_moved:
            gold_room()
        elif choice=="Help":
            print(" Options are as follows : 1. Take Honey, 2. Taunt Bear, 3. Take Bear ")
        else:
            print("I got no idea what that means. ")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    cthulu_moved=False


    while True:
       choice=input("> ")
       if "flee" in choice:
         print("Nice Choice!")
         cthulu_moved=True
         start()
       elif "head" in choice:
        dead("Well that was tasty!")
        cthulu_moved=True
       elif choice=="Help":
        print(" Options are flee or head ")
       else:
        cthulhu_room()


def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    choice_made=False


    while True:
       choice=input("> ")
       if choice=="left":
        choice_made=True
        bear_room()
       elif choice=="right":
         choice_made=True
         cthulhu_room()
       elif choice=="Help":
         print("Valid options are left and right")
         choice_made=True
         start()
       else:
        dead("You stumble around the room until you starve. ")

print("Enter Help at choice if you want to look at valid answers at any point.")

start()

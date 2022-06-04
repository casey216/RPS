import random

def main():
    options = ["R","P","S"]
    hand = ""
    
    while hand not in options:
        if hand != "":
            print(f"You chose a wrong option. Try again.")

        hand = input("Welcome to Rock, Paper, Scissors! Type R, P or S to play: \n")
        hand = hand.capitalize()

    com = random.choice(options)

    
    if hand == com:
        print("The computer and player pick the same move")
        main()

    if hand == "R":
        if com == "P":
            print("Player(Rock) : CPU(Paper).\nThe winner is CPU")
        if com == "S":
            print("Player(Rock) : CPU(Scissors).\nThe winner is Player")

    if hand == "P":
        if com == "R":
            print("Player(Paper) : CPU(Rock).\nThe winner is Player")
        if com == "S":
            print("Player(Paper) : CPU(Scissors).\nThe winner is CPU")

    if hand == "S":
        if com == "R":
            print("Player(Scissors) : CPU(Rock).\nThe winner is CPU")
        if com == "P":
            print("Player(Scissors) : CPU(Paper).\nThe winner is Player")
            
main()

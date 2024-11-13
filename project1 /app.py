def start_adventure():
    print("Welcome to the Adventure!")
    print("You find yourself in a dark forest.")
    print("You can go 'left' or 'right'.")

    choice = input("> ").lower()

    if choice == "left":
        print("You encounter a friendly dragon!")
        print("The dragon offers you treasure. Do you 'take' it or 'decline'?")

        dragon_choice = input("> ").lower()
        if dragon_choice == "take":
            print("You take the treasure and escape the forest, rich and happy!")
        elif dragon_choice == "decline":
            print("The dragon is insulted and attacks! You're defeated.")
        else:
            print("Invalid choice. You're lost in the forest.")
    elif choice == "right":
        print("You stumble upon a hidden cave.")
        print("Inside, you find a magical sword. Do you 'take' it or 'leave' it?")

        sword_choice = input("> ").lower()
        if sword_choice == "take":
            print("You take the sword and become a powerful knight!")
        elif sword_choice == "leave":
            print("You leave the sword and continue exploring.")
        else:
            print("Invalid choice. You're lost in the cave.")
    else:
        print("Invalid choice. You're lost in the forest.")

start_adventure()
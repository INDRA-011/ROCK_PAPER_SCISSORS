import random 

def playGame():
    options = ['rock', 'paper', 'scissors']

    while True:
        print("\n choose one: rock/paper/scissors (OR 'quit' to exit)")
        user_choice = input("enter the option you like: ").lower().strip()

        if user_choice == "quit":
            print("thanks for playing. ")
            break

        if user_choice not in options: 
            print("invalid input: choose again: ")
            continue

        computer_choice = random.choice(options)
        print(f"your choice: {user_choice.capitalize()}")
        print(f"computer choice: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            print("ITs a TIE")

        elif(
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock")or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("YOU WON !!!!!")

        else: 
            print("YOU LOSE !!!!")

        
playGame()

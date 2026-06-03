import random

def play_rps():
    options = ["rock", "paper", "scissors"]

    print("WELCOME TO THE GAME")
    
    while True:
        print("\nChoose one: rock / paper / scissors (or 'quit' to exit)")
        user_choice = input("Your choice: ").strip().lower()

        if user_choice == "quit":
            print("\nThanks for playing! Goodbye 👋")
            break

        if user_choice not in options:
            print("❌ Invalid choice! Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"\n🧑 You chose   : {user_choice.capitalize()}")
        print(f"🤖 Computer chose: {computer_choice.capitalize()}")

        # Determine result
        if user_choice == computer_choice:
            print("\n🤝 It's a TIE!")
        elif (
            (user_choice == "rock"     and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper")    or
            (user_choice == "paper"    and computer_choice == "rock")
        ):
            print("\n🎉 SUCCESS! You WIN!")
        else:
            print("\n💀 You LOSE! Better luck next time.")

        print("-" * 35)

if __name__ == "__main__":
    play_rps()
#Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

choices = (
    f"The computer chose {computer_choice}\n"
    f"You chose {user_choice}")

print(choices)

# Run Conditionals

if computer_choice == "r" and user_choice == "p":
    print("YOU WON!")
elif computer_choice == "r" and user_choice == "s":
    print("YOU LOST!")
elif computer_choice == "P" and user_choice == "s":
    print("YOU WON")
elif computer_choice == "p" and user_choice == "r":
    print("YOU LOST")
elif computer_choice == "s" and user_choice == "p":
    print("YOU LOST")
elif computer_choice == "s" and user_choice == "r":
    print("YOU WON")
elif computer_choice == "s" and user_choice == "s":
    print("YOU TIED")
elif computer_choice == "p" and user_choice == "p":
    print("YOU TIED")
elif computer_choice == "r" and user_choice == "r":
    print("YOU TIED")
else: 
    print("I dont understand that!")
    print("Next time, choose from 'r', 'p', or 's'.")

    
    
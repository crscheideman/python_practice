# Initial variable to track game play
user_play = "y"

# set start and last number
start_number = 0

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_number = input("How many numbers?")

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(start_number, int(user_number) + start_number):

        # Print each number in the range
        print(x)

    # set the next start number 
    start_number = start_number + int(user_number)
    5
    # Once complete...
    user_play = input("Continue: (y)es or (n)o?")
    
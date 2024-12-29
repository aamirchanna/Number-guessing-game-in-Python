import random

print("----------------------------------------------")
print("\tWelcome to guessing number game")
print("----------------------------------------------")

ran_num = random.randint(1, 15)

guess = None
attempts = 0

while (guess != ran_num):
    try:
        guess = int(input("Please guess the number : "))
        attempts += 1

        if(guess > ran_num):
            print("To high! Try again")
        elif(guess < ran_num):
            print("To low! Try again")
        else:
            print(f"Congrates! you have guessed the number {ran_num} in {attempts} attempts")

    except:
        print("Error! please enter integer")

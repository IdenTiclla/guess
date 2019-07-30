from colorama import Fore, Style
import random

def main():
    min_number = 1
    max_number = 20
    guess_taken = 0
    username = input("Hello what is your name?: ")
    random_number = random.randint(min_number, max_number)

    print(Fore.YELLOW + f"Well, {username}. I am thinking in a number between {min_number} and {max_number}")
    print(Style.RESET_ALL)

    while guess_taken < 6:
        guess = int(input("Take a guess: "))
        guess_taken += 1
        if guess < random_number:
            print(Fore.RED + "Your guess is too Low.")
            print(Style.RESET_ALL)
        elif guess > random_number:
            print(Fore.RED + "Your guess is too High.")
            print(Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"Good Job, {username}! you guessed my number in {guess_taken}")
            print(Style.RESET_ALL)
            break
    if guess_taken == 6:
        print(Fore.RED + f"No the number I was thinking of was {random_number}")
        print(Style.RESET_ALL)

if __name__ == "__main__":
    main()

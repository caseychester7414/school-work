import random
number = random.randint(1,9)

def guessingloop():
    answer = random.randint(1,9)
    guess = int(input("Please guess any number between 1 and 9: "))
    trys = 0
   
    while True:
        if(guess == answer):
            print(f"you got it right!! The number is {answer}")
            print(f'You used {trys} trys!')
            break
        if(guess < answer):
            print(f"try again! you got it incorrect")
            trys = trys + 1
            print(f"You have tried {trys} times!")
            print(answer)
            play = input("Wanna keep playing? Yes to continue. exit to quit. ")
            if(play == 'yes'):
                guess = int(input("Please try to guess a number between 1 and 9: "))
            elif(play == 'exit'):
                print("See ya!!!")
                break
        if(guess > answer):
            print(f'OPPS . That number was way too high. Try again')
            trys = trys + 1
            print(f"You've guessed {trys} times!")
            print(answer)
            play = input("Wanna keep playing? Yes to continue. exit to quit. ")
            if(play == 'yes'):
                guess = int(input("Please guess any number between 1 and 9: "))
            elif(play == 'exit'):
                print("hope to see you soon!")
                break

guessingloop()
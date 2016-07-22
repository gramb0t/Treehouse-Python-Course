import random

def win(secret_num, tries) :
    print("YEAH!!! you got it! the secret number was {}".format(secret_num))
    print("only took you {} tries!".format(tries))

def game() :
    # make a random number between 1-10
    secret_num = random.randint(1, 10)
    tries = 1
    
    #limit number of guesses
    #catch type error
    #give direction (too high, too low)
    #let people re-play
    
    
    #game loop
    while True:
        # get guess
        try :
            guess = int(input("Guess a number! keep it between 1-10  > "))

        except ValueError :
            print("a number please, only a number, get outta here with your 'letters'!")
            continue
        
        # compare
        if guess == secret_num :
            win(guess, tries)
            break
        else :
            if tries == 5 :
                print("lol nope, and your done. 5 tries is enough.")
                again = input("wanna try again? y/n  > ")
                if again == 'y' or 'Y' :
                    game()
                else :
                    print("well thanks for playing anyway!")
                    break
            else:
                print("nope! suckah!")
                tries += 1
                    

game()

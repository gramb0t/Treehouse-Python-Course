import random

def win(secret_num, tries) :
    print("YEAH!!! you got it! the secret number was {}".format(secret_num))
    print("only took you {} tries!".format(tries))

def too_high() :
    print("too high fool")
    tries+=1

def too_low() :
    print("nope! suckah! too low!")
    tries += 1      

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
        # make safe int
        try :
            #get guess
            guess = int(input("Guess a number! keep it between 1-10  > "))
        except ValueError :
            print("{} isnt number please, only a number, get outta here with your 'letters'! \r\n".format(guess))
            continue
        else :
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
                    elif again == 'n' or 'N' :
                        print("well thanks for playing anyway!")
                        break
                else:
                    if guess > secret_num :
                        too_high()
                    else:
                        too_low()
                    

game()

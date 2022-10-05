import random
import sys
#Declare the Class for the Random Guessing game
class GuessingGame:
#This is the constructor for the class.
    def __init__(self):
        ## The Random range
        self.From = 1
        self.To = 10000

    ## Function to generate the random number to be guessed.
    def get_random_number(self):
        return random.randint(self.From, self.To)

    ## the function for the game
    def game(self):
        ## get the random number
        random_number = self.get_random_number()
        #If the number is found then the game is over.
        gameover = True
        print("Guess the randomly generated number from 1 to 10000")

        #Run the game until the random number is found
        while gameover:
            user_no = int(input("Enter the guessed number: "))
            #Check if the user number equals the Random Number
            if user_no == random_number:
                print("-> Congratulations! You got it.")
                gameover = False
            elif user_no < random_number:
                print("-> Your number is less than the random number")
            else:
                print("-> Your number is greater than the random number")

## instantiating and starting the game
numberGuessingGame = GuessingGame()
#numberGuessingGame.game()
print("The size of the function is:" + str(sys.getsizeof(numberGuessingGame.game())))

##This section contains code snippets for the database class.


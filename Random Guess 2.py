import sys

high = 10000
low = 0
numberGuess = (high + low) / 2
print("User, guess a number between 1 and 10000")
while True:
    print("Are you thinking of the number: ", numberGuess)
    userInput = input("Enter yes/higher/lower: ")
    if userInput == "lower":
        high = numberGuess
        numberGuess = (numberGuess - low) // 2 + low
    elif userInput == "higher":
        low = numberGuess
        numberGuess = (high - numberGuess) // 2 + numberGuess
    elif userInput == "yes":
        print("\nCongrats, your number was guessed!")
        break

print("Memory size of high: ", sys.getsizeof(high))
print("Memory size of low: ", sys.getsizeof(low))
print("Memory size of guess: ", sys.getsizeof(numberGuess))
print("Memory size of userInput: ", sys.getsizeof(userInput))
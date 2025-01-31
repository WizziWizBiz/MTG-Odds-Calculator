"""This program prompts inputs for number of cards that the user wants to play on turns 1-4, and the number of lands in the deck.
  The program then calculates the odds of playing a land and a card on turns 1-5, with turn 5 being the commander.
  It will then output this result, along with the number of remaining slots in the deck for other cards (e.g. removal, draw, etc.)."""

import pandas as pd

#open CSV files as lists
cards_probability = pd.read_csv('CardsProbability.csv').values.tolist()
lands_probability = pd.read_csv('LandsProbability.csv').values.tolist()

#TODO: write isValidInput function
def isValidInput(t1, t2, t3, t4, lands):
    """Checks to see if each number entered is a valid integer, and returns the corresponding boolean."""
    return True

print("Welcome to the 5 mana commander calculator!")
while True:
    #prompt user for all inputs
    num_turn1 = int(input("Please enter the number of turn 1 plays: "))
    num_turn2 = int(input("Please enter the number of turn 2 plays: "))
    num_turn3 = int(input("Please enter the number of turn 3 plays: "))
    num_turn4 = int(input("Please enter the number of turn 4 plays: "))
    num_lands = int(input("Please enter the number of lands: "))
    cards_remaining = 99 - (num_lands + num_turn1 + num_turn2 + num_turn3 + num_turn4)

    #check input validity
    if not isValidInput(num_turn1, num_turn2, num_turn3, num_turn4, num_lands):
        print("One or more numbers was not valid. Please try again.")
        continue

    #output individual validities
    probability1 = cards_probability[num_turn1 - 1][1]
    print("Likelihood of turn 1 success:", probability1 * 100)
    probability2 = cards_probability[num_turn2 - 1][2]
    print("Likelihood of turn 2 success:", probability2 * 100)
    probability3 = cards_probability[num_turn3 - 1][3]
    print("Likelihood of turn 3 success:", probability3 * 100)
    probability4 = cards_probability[num_turn1 - 1][4]
    print("Likelihood of turn 4 success:", probability4 * 100)
    probability_lands = lands_probability[num_lands - 1][1]
    print("Likelihood of enough lands", probability_lands * 100)


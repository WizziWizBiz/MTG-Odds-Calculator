"""This program has 2 modes: manual and brute_force. It will either use 1 set of values or brute force a range of values
  The program then calculates the odds of playing a land and a card on turns 1-5, with turn 5 being the commander.
  It will then output this result, along with the number of remaining slots in the deck for other cards (e.g. removal, draw, etc.)."""
from time import sleep
import pandas as pd

def is_valid_input(t1, t2, t3, t4, lands):
    """Checks to see if each number entered is a valid integer, and returns the corresponding boolean."""
    if 1<=t1<=15 and 1<=t2<=15 and 1<=t3<=15 and 1<=t4<=15 and 30<=lands<=45:
        return True
    return False


def manual_output():
    """prompts user for necessary inputs for 1 set of calculations, does the calculations, and outputs results."""

    # prompt user for all inputs
    num_turn1 = int(input("Please enter the number of turn 1 plays: [1-15] "))
    num_turn2 = int(input("Please enter the number of turn 2 plays: [1-15] "))
    num_turn3 = int(input("Please enter the number of turn 3 plays: [1-15] "))
    num_turn4 = int(input("Please enter the number of turn 4 plays: [1-15] "))
    num_lands = int(input("Please enter the number of lands: [30-45] "))

    # check input validity
    if not is_valid_input(num_turn1, num_turn2, num_turn3, num_turn4, num_lands):
        print("One or more numbers was not valid. Please try again.")

    # output individual chances
    probability1 = cards_probability[num_turn1 - 1][1]
    print("\nLikelihood of turn 1 success:", probability1 * 100)
    probability2 = cards_probability[num_turn2 - 1][2]
    print("Likelihood of turn 2 success:", probability2 * 100)
    probability3 = cards_probability[num_turn3 - 1][3]
    print("Likelihood of turn 3 success:", probability3 * 100)
    probability4 = cards_probability[num_turn1 - 1][4]
    print("Likelihood of turn 4 success:", probability4 * 100)
    probability_lands = lands_probability[num_lands - 30][1]
    print("Likelihood of enough lands", probability_lands * 100)

    sleep(delay_time)

    # overall results
    overall_probability = probability1 * probability2 * probability3 * probability4 * probability_lands
    overall_probability = round(overall_probability, 3)
    cards_remaining = 99 - (num_lands + num_turn1 + num_turn2 + num_turn3 + num_turn4)

    print("\nOverall likelihood of success:", overall_probability * 100)
    if overall_probability >= good_probability:
        print("This is a good result!")
    else:
        print("This is probably not good enough")
    print("Card slots remaining:", cards_remaining)

#TODO: TEST IT
def brute_force(mincards, maxcards, lands=38):
    """Takes a minimum and maximum range for the cards per turn (shared for all 4 slots) and does the calculations for every permutation within that range.
       It will then output each permutation that has a higher probability of success than good_probability"""

    combos = []
    for card1 in range(mincards, maxcards + 1):
        for card2 in range(mincards, maxcards + 1):
            for card3 in range(mincards, maxcards + 1):
                for card4 in range(mincards, maxcards + 1):
                    probability1 = cards_probability[card1 - 1][1]
                    probability2 = cards_probability[card2 - 1][2]
                    probability3 = cards_probability[card3 - 1][3]
                    probability4 = cards_probability[card4 - 1][4]
                    probability_lands = lands_probability[lands - 30][1]
                    overall_probability = probability1 * probability2 * probability3 * probability4 * probability_lands
                    if overall_probability >= good_probability:
                        combos.append([probability1, probability2, probability3, probability4, probability_lands])
    for combo in combos:
        print(combo)


delay_time = 1.5
good_probability = 0.175

#open CSV files as lists
cards_probability = pd.read_csv('CardsProbability.csv').values.tolist()
lands_probability = pd.read_csv('LandsProbability.csv').values.tolist()


print("Welcome to the 5 mana commander calculator!")

while True:
    modality = int(input("Input 1 for manual, 2 for brute force, 3 to quit"))
    if modality == 1:
        manual_output()
        sleep(delay_time)
    elif modality == 2:
        minimum_cards = int(input("Low end of range? [1-15]"))
        maximum_cards = int(input("High end of range? [1-15]"))
        brute_force(minimum_cards, maximum_cards)
        sleep(delay_time)
    elif modality == 3:
        break

print("Thank you for using this program :) have a nice day")
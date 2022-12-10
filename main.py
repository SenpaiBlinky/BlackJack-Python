## The deck is unlimited in size. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo
import os

def return_score(player):
    return sum(player)

def blackjack():
    os.system('cls')

    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    dealer_cards = []
    busted = False
    replay = False

    # game init
    for i in range(0,2):
        player_cards.append(cards[random.randint(0,12)])
        dealer_cards.append(cards[random.randint(0,12)])

    print(f"These are your cards {str(player_cards)}")
    print("This is the dealers card " + str(dealer_cards[0]))
    hit_or_stand = input("Would you like to hit or stand? Type 'hit' or 'stand' respectively ")

    while hit_or_stand == "hit":
        player_cards.append(cards[random.randint(0,12)])
        print(f"These are your cards {str(player_cards)}")
        print("This is the dealers card " + str(dealer_cards[0]))
        
        if return_score(player_cards) > 21:
            print(f"You have {sum(player_cards)} You busted :(. L RIP BOZO")
            busted = True
            break
        else:
            hit_or_stand = input("Would you like to hit or stand? Type 'hit' or 'stand' respectively ")

            

    if busted == False:
    # RESULTS
        while sum(dealer_cards) < 17:
            dealer_cards.append(cards[random.randint(0,12)])
            
        if sum(dealer_cards) > 21:
            print("Dealer busted, you win :)")
        else:
            if sum(player_cards) > sum(dealer_cards):
                print(f"You have {sum(player_cards)} and Dealer has {sum(dealer_cards)} Woot Woot, You Win!!!")
            elif sum(player_cards) == sum(dealer_cards):
                print(f"You have {sum(player_cards)} and Dealer has {sum(dealer_cards)} You Tied :|")
            else:
                print(f"You have {sum(player_cards)} and Dealer has {sum(dealer_cards)} You Lost :(. L RIP BOZO")
    
    replay = input("Would you like to play again? 'Y' or 'N' ")
    if replay == "y":
        blackjack()

blackjack()

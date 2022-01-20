import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def player_sum(card_list):
    sum = 0
    for card in card_list:
        sum += card
    return sum

def totals ():
    print(f"Your cards:{player_card_list}. Current score: {player_sum(player_card_list)}")
    print(f"Dealer's first card:{dealer_card_list}. Current score: {player_sum(dealer_card_list)}")

def dealer(): 
    dealer_cards = player_sum(dealer_card_list)
    while dealer_cards <= 16:
        dealer_card_list.append(random.choice(cards))
        if 11 in dealer_card_list and player_sum(dealer_card_list) >= 22:
            for i in range(0,len(dealer_card_list)):
                if dealer_card_list[i] == 11:
                    dealer_card_list[i] = 1
        dealer_cards = player_sum(dealer_card_list)
    print(f"Computer's final hand {dealer_card_list}, final score: {player_sum(dealer_card_list)}")

decision = 'y'
while decision == 'y':

    player_card1 = random.choice(cards)
    player_card2 = random.choice(cards)
    player_card_list = [player_card1,player_card2]

    dealer_card1 = random.choice(cards)
    dealer_card_list = [dealer_card1]

    decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    totals()

    more_cards = 'y'
    while more_cards == 'y':
        more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
        if more_cards == "y":
            player_card_list.append(random.choice(cards))
            if 11 in player_card_list and player_sum(player_card_list) >= 22:
                for i in range(0,len(player_card_list)):
                    if player_card_list[i] == 11:
                        player_card_list[i] = 1
            if player_sum(player_card_list) >= 21:
                more_cards = "n"
            totals()
        if more_cards == "n":
            print(f"Your final hand {player_card_list}, final score: {player_sum(player_card_list)}")
            dealer()
            if player_sum(player_card_list) > player_sum(dealer_card_list) and player_sum(player_card_list) <= 20:
                print("You Win!")
            elif player_sum(player_card_list) == player_sum(dealer_card_list):
                print("It'a Push!")
            elif player_sum(player_card_list) < player_sum(dealer_card_list) and player_sum(dealer_card_list) <= 20:
                print("You Lose!")
            elif player_sum(player_card_list) == 21 and player_sum(dealer_card_list) != 21:
                print("BlackJack! You win!")
            elif player_sum(dealer_card_list) == 21 and player_sum(player_card_list) < 21:
                print("Dealer has BlackJack! You lose!")
            elif player_sum(dealer_card_list) > 21 and player_sum(dealer_card_list) > player_sum(player_card_list):
                print("You Win!")
            elif player_sum(player_card_list) > 21 and player_sum(player_card_list) > player_sum(dealer_card_list):
                print("You went over! You Lose!")




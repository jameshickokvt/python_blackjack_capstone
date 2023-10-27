

def blackjack():
    '''Starts a brand new game of blackjack'''
    import random
    import time
    #from art import logo

    logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                  
    print(logo)

    #Initial conditions of every new game
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    dealer_cards = []

    player_turn = True
    dealer_turn = False

    player_win = False
    dealer_win = False

    #Blackjack specific functions
    def deal(deck):
        '''Adds one random card to chosen deck'''
        deck.append(random.choice(cards))

    def show_all_cards():
        '''Shows current cards and scores of both players'''
        print(
            f"Your cards: {player_cards}, current score: {score_of_cards(player_cards)}"
        )
        print(
            f"The dealer's cards: {dealer_cards}, current score: {score_of_cards(dealer_cards)}"
        )
        time.sleep(3)

    def show_cards_player_perspective():
        '''Shows current cards and score of player, and the first card of the dealer'''
        print(
            f"Your cards: {player_cards}, current score: {score_of_cards(player_cards)}"
        )
        print(f"The dealer's first card: {(dealer_cards)[0]}")

    def only_player_cards():
        print(f"Your cards: {player_cards}")

    def score_of_cards(deck):
        '''Returns score of cards. Special conditions if there is an ace(11) in their hand'''
        if sum(deck) > 21:
            for card in deck:
                if card == 11:
                    deck.remove(11)
                    deck.append(1)
        return sum(deck)

    #Initial deal - game begins
    deal(player_cards)
    deal(player_cards)
    deal(dealer_cards)
    deal(dealer_cards)

    #First phase of the game where player chooses to hit or stay. Game ends if they bust.
    while player_turn == True:
        score_of_cards(player_cards)

        #Check if player busts before continuing
        if score_of_cards(player_cards) > 21:
            only_player_cards()
            print(f"Player bust! Your score is {score_of_cards(player_cards)}.")
            player_turn = False
            dealer_win = True

        #Check if player hits 21, ends player turn
        elif score_of_cards(player_cards) == 21:
            only_player_cards()
            print("Lucky 21!")
            player_turn = False
            dealer_turn = True

        #Player chooses to hit or stay
        else:
            show_cards_player_perspective()
            player_hit = input("Hit or stay? ").lower()
            if player_hit == "hit":
                deal(player_cards)
            else:
                player_turn = False
                dealer_turn = True

    #Second phase where dealer plays if the dealer did not bust in the first phase.
    while dealer_turn == True:
        print("The dealer flips their card.... ")
        time.sleep(.5)
        print((dealer_cards)[-1])
        show_all_cards()
        #The dealer must draw on 16 or under and must stand on 17 or over
        while score_of_cards(dealer_cards) < 17:
            print("The dealer hits.")
            deal(dealer_cards)
            print(f"They get a {(dealer_cards)[-1]}.")
            show_all_cards()

        #Determing who wins
        if score_of_cards(dealer_cards) > 21:
          print(f"Dealer bust!  Their score is {score_of_cards(dealer_cards)}.")
          player_win = True
        elif score_of_cards(dealer_cards) >= score_of_cards(
                player_cards) and score_of_cards(dealer_cards) <= 21:
            dealer_win = True
        else:
            player_win = True
        dealer_turn = False

    #End of game
    if dealer_win == True:
        print("You lose.")
    elif player_win == True:
        print("You win!")

  
    if input("Do you want to play again? Type 'y' or 'n': ").lower() == 'y':
        blackjack()
    else:
      print("Goodbye.")


#Prompt users to start game
if input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower(
) == 'y':
    blackjack()
else:
    print("That's probably a good idea, gambling is immoral.")


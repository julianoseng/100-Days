#Blackjack

#Need random cards dealt
import random
import time

players_hand = []
dealers_hand = []
players_hand_total = 0
dealers_hand_total = 0
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

print("Welcome to Blackjack!\n")

def game_over():
    global players_hand
    global dealers_hand
    if input("Do you want to go again? Type 'y' or 'n' : ") == 'y':
            print("")
            players_hand = []
            dealers_hand = []
            start_game()


#Calculates hand totals
def get_hand_total(hand):
    hand_total = 0
    for card in hand:
        hand_total += card
    return hand_total


def start_game():
    # Could be a bug later!
    while len(players_hand) != 2:
        # Chooses random card from the deck
        card_dealt_rand_select = random.randint(0,len(cards)-1)
        # gives random card to players hand
        players_hand.append(cards[card_dealt_rand_select])
    #Figures the total for the players hand
    players_hand_total = get_hand_total(players_hand)
    
    while len(dealers_hand) != 1:
        card_dealt_rand_select = random.randint(0,len(cards)-1)
        #Add top card to dealers hand
        dealers_hand.append(cards[card_dealt_rand_select])
    dealers_hand_total = get_hand_total(dealers_hand)
    
    if players_hand_total == 21:
        print(f"You were dealt {players_hand} for a total of {players_hand_total}")
        print("You got a blackjack! You win this round!")
        game_over()
    else:
        print(f"The dealer's top card is {dealers_hand}")
        print(f"You were dealt {players_hand} for a total of {players_hand_total}")
        game_continue()


def game_continue():
    global players_hand_total
    continue_playing = True
    
    while continue_playing == True:
        hit_or_stay = input("Type 'h' to hit or type 's' to stay :")
        if hit_or_stay == 'h':
            card_dealt = 0
            card_dealt_rand_select = random.randint(0,len(cards)-1)
            
            # This is when the ace turns from a 1 to an 11
            # Appends a 1 to the list instead of an 11
            if cards[card_dealt_rand_select] == 11 and 11 + players_hand_total > 21:
                players_hand.append(1)
                card_dealt = 1    
            else: #Appends an 11 to the players hand list (normal flow)
                players_hand.append(cards[card_dealt_rand_select])
                card_dealt = cards[card_dealt_rand_select]
            # Calculates the players_hand_total
            players_hand_total = get_hand_total(players_hand)
            
            print(f"\nYou were dealt a {card_dealt} for a total of {players_hand_total}")
            print(f"In your hand: {players_hand}")
        elif hit_or_stay == 's':
            continue_playing = False
            dealers_turn()
        
        if players_hand_total > 21:
            continue_playing = False
            print("You busted!")
            game_over()
                
    
            
def dealers_turn():
    card_dealt = 0
    
    print("\nThis is the dealers turn")
    card_dealt_rand_select = random.randint(0,len(cards)-1)
    dealers_hand.append(cards[card_dealt_rand_select])
    dealers_hand_total = get_hand_total(dealers_hand)
    print(f"Dealer flips a {cards[card_dealt_rand_select]} for a total of {dealers_hand_total}...")
    print(f"The dealers hand: {dealers_hand}\n")
    time.sleep(2)
    if dealers_hand_total == 21:
        print("Dealer wins with a blackjack. Awe man!")
        game_over()

    while dealers_hand_total < 17:
        card_dealt_rand_select = random.randint(0,len(cards)-1)
        
        if cards[card_dealt_rand_select] == 11 and 11 + dealers_hand_total > 21:
            dealers_hand.append(1)
            card_dealt = 1
        else: #Appends an 11 to the players hand list (normal flow)
            dealers_hand.append(cards[card_dealt_rand_select])
            card_dealt = cards[card_dealt_rand_select]
        
        dealers_hand_total = get_hand_total(dealers_hand)
        print(f"Dealer flips a {card_dealt} for a total of {dealers_hand_total}...")
        print(f"The dealers hand: {dealers_hand}\n")
        
        
        
        time.sleep(2)
        
    players_hand_total = get_hand_total(players_hand)
    dealers_hand_total = get_hand_total(dealers_hand)
    
    if dealers_hand_total > 21:
        print("Dealer busts. You win!")
        game_over()
    elif dealers_hand_total == players_hand_total:
        print("Draw.\n")
        game_over()
    elif dealers_hand_total > players_hand_total:
        print("Dealer wins")
        game_over()
    elif players_hand_total > dealers_hand_total:
        print("You win!")
        game_over()
    

start_game()

# #hit or stay

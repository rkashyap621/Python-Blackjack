import random
import Card_Setup as Cards

def deck_setup():
    deck=list(Cards.Single_Deck.keys())
    return deck


def initial_deal():
    dealer=[]
    player=[]
    new_deck = deck_setup()
    print("Card Deck is ready!")
    for i in range(random.randint(3,10)):
        random.shuffle(new_deck)
    print("Card Deck Shuffling is done!")
    idx=0
    for i in range(2):
        dealer+=[new_deck[idx]]
        new_deck.pop(idx)
        player+=[new_deck[idx]]
        new_deck.pop(idx)
    print("Dealer:",dealer[0])
    print("Player:",player)
    print("Dealt Cards:", len(dealer) + len(player))
    print("Remaining Cards:", len(new_deck))
    return dealer,player,new_deck


def init_deal_score(player, dealer):
    dealer_score=0
    player_score=0
    num_Ace_Cards=0
    dealer_score+=Cards.Single_Deck[dealer[0]]
    for card in player:
        if card in Cards.Ace_Cards:
            num_Ace_Cards+=1
        player_score+=Cards.Single_Deck[card]
    if num_Ace_Cards==2:
        player_score-=10
    return dealer_score,player_score


def initial_check(player_score, dealer_score,dealer,player):
    dealer_true_score=0
    num_Ace_Cards = 0
    for card in dealer:
        if card in Cards.Ace_Cards:
            num_Ace_Cards+=1
        dealer_true_score+=Cards.Single_Deck[card]
    if num_Ace_Cards==2:
        dealer_true_score-=10
    if player_score==21 or dealer_true_score==21:
        if dealer_true_score==player_score:
            print("It's a Push! Dealer also has a Blackjack!. Nobody wins!🤔")
            print("Dealer:", dealer)
            player("Player:", player)
            return False
        elif dealer_true_score>player_score:
            print("That's a Blackjack! Uh-Oh! The Dealer wins.😭")
            print("Dealer:", dealer)
            player("Player:", player)
            return False
        elif dealer_true_score<player_score:
            print("That's a Blackjack!The Player wins.🤯")
            print("Dealer:", dealer)
            player("Player:", player)
            return False
    else:
        return True


def hit_action(dealer,player,remdeck):
    idx=0
    new_card=remdeck[idx]
    remdeck.pop(idx)
    player.append(new_card)
    print("Dealer:", dealer[0])
    print("Player:", player)
    print("Dealt Cards:", len(dealer) + len(player))
    print("Remaining Cards:", len(remdeck))
    return remdeck,player, True


def player_bust_check(dealer,player,dealer_score, player_hit, dealer_hit):
    if not player_hit and not dealer_hit:
        print("Dealer:", dealer)
        print("Player:", player)

    player_true_score=0
    for card in player:
        if card in Cards.Ace_Cards:
            player_true_score+=1
        else:
            player_true_score+=Cards.Single_Deck[card]

    if player_true_score>21:
            print("Oh no! Player is Busted.😭 The Dealer Wins.", "Player Score: "+ str(player_true_score)+" "+"Dealer Score: "+ str(dealer_score))
            return False, True, player_true_score
    elif player_true_score==21:
        print("Woohoo! Player Wins.😎 Dealer is lost.", "Player Score: "+ str(player_true_score)+" "+"Dealer Score: "+ str(dealer_score))
        return False, True, player_true_score
    else:
        print("Dealer's Score:", dealer_score)
        print("Player's Score:", player_true_score)
        return True, False, player_true_score


def dealer_score(dealer):
    dealer_true_score=0
    for card in dealer:
        if card in Cards.Ace_Cards:
            dealer_true_score+=1
        else:
            dealer_true_score+=Cards.Single_Deck[card]
    return dealer_true_score


def self_hit(dealer,player, remdeck):
        idx = 0
        new_card = remdeck[idx]
        remdeck.pop(idx)
        dealer.append(new_card)
        print("Dealer:", dealer)
        print("Player:", player)
        print("Dealt Cards:", len(dealer) + len(player))
        print("Remaining Cards:", len(remdeck))
        return dealer, remdeck, True
        
def dealer_bust_check(dealer,player,player_score, dealer_score, player_hit, dealer_hit):
    if not player_hit or not dealer_hit:
        print("Dealer:", dealer)
        print("Player:", player)
    if dealer_score==21:
        print("Oh My! Dealer Wins!😭", "Player Score: "+ str(player_score)+" "+"Dealer Score: "+ str(dealer_score))
        return True
    elif dealer_score>21:
        print("Yeah! Dealer Busted! Player Wins!😎", "Player Score: "+ str(player_score)+" "+"Dealer Score: "+ str(dealer_score))
        return True
    else:
        if dealer_score==player_score:
            print("It's a Push! Nobody wins!🤔", "Player Score: "+ str(player_score)+" "+"Dealer Score: "+ str(dealer_score))
            return True
        else:
            if dealer_score>player_score:
                print("Alas! Dealer Wins!😭", "Player Score: "+ str(player_score)+" "+"Dealer Score: "+ str(dealer_score))
                return True
            if dealer_score<player_score:
                print("Oh! Yes!! Player Wins!😎", "Player Score: "+ str(player_score)+" "+"Dealer Score: "+ str(dealer_score))
                return True

import Blackjack_ASCII_Art as Art
import Dealer_Mechanism as Dealer

print(Art.logo)
print("Welcome to Pythonista Black Jack Game!\n")

start=input("Hi Player! Are you ready to start?(yes/no)\n")

player=[]
dealer=[]
deck=[]
should_continue=0
game_over=False
player_sc=0
dealer_sc=0
player_hit=False
dealer_hit=False

if start=="yes":
    [dealer, player, deck]=Dealer.initial_deal()
    [dealer_sc, player_sc]=Dealer.init_deal_score(player, dealer)
    print("Dealer's Score:", dealer_sc)
    print("Player's Score:", player_sc)
    should_continue=Dealer.initial_check(player_sc, dealer_sc, dealer, player)

while should_continue==True and not game_over:
    player_decision=input("Would you like to 'Hit' or 'Stand'? Type 'y' to 'Hit' or 'n' to 'Stand':\n")
    if player_decision=="y":
        [deck, player, player_hit]=Dealer.hit_action(dealer, player, deck)
        [should_continue, game_over, player_sc]=Dealer.player_bust_check(dealer, player, dealer_sc, player_hit, dealer_hit)

    elif player_decision=="n":
        dealer_sc=Dealer.dealer_score(dealer)

        while dealer_sc<17 and not game_over:
            [dealer, deck, dealer_hit]=Dealer.self_hit(dealer, player, deck)
            dealer_sc = Dealer.dealer_score(dealer)
        game_over=Dealer.dealer_bust_check(dealer, player, player_sc, dealer_sc, player_hit, dealer_hit)

#!/usr/bin/python3
import random
from os import system
from collections import deque

class Card:

    range_of_values = (2, 15)
    suits = set(["spades", "hearts", "clubs", "diamonds"])
    values = set([i for i in range(*range_of_values)])
    names = {11: "jack", 12: "queen", 13: "king", 14: "ace"}

    def __init__(self, value, suit):
        if value in self.values:
            self.face_value = value
        else:
            raise ValueError("Invalid Card Value {0}".format(value))
        if suit in self.suits:
            self.suit = suit
        else:
            raise ValueError("Invalid Suit {0}".format(suit))

    def __repr__(self):
        try:
            val = Card.names[self.face_value]
        except KeyError:
            val = str(self.face_value)
        return "{0} of {1}".format(val, self.suit) 


class CardDeck:

    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for val in Card.values:
                self.cards.append(Card(val, suit))


class BlackJackPlayer:

    def __init__(self, name, money=0, dealer=False):
        self.name = name
        self.money = float(money)
        self.dealer = dealer
        self.hand = []
        self.first_card = 0

    def reset_hand(self):
        self.hand = []
        self.bet = 0
        self.first_card = 0

    def deal(self, card):
        self.hand.append(card)

    def collect_from(self, players, winners):
        for p in players:
            self.money += p.bet / winners
            p.money -= p.bet / winners


    def hand_value(self):
        return BlackJackGame.get_hand_value(self.hand)


    def show_hand(self, final=False):
        if final:
            hand = self.hand
            hand_value = self.hand_value()
        else:
            hand = []
            hand_value = BlackJackGame.get_hand_value(self.hand)
            for h in self.hand:
                hand.append(h)
                if self.dealer:
                    hand_value = ">=" + str(BlackJackGame.get_hand_value(hand))   
                    hand.append("Unknown")
                    break 



        base_str = "{0} has {1}. ({2}) ({3})".format(self, hand, hand_value, self.bet)
        if self.hand_value() > 21:
            base_str += " (Busted!)"

        print(base_str)

    def __repr__(self):
        return self.name

class BlackJackGame:

    dealer_name = "Dealer"

    def create_except_msg(self, msg):
        return self.__class__.__name__ + "must be played with at least 1 player"

    def __init__(self, players=None, number_of_decks=1, reshuffle_threshold=0, min_bet=0, dealer_start=100000):
        self.players = {}
        if not len(players):
            raise ValueError(self.create_except_msg("Must be played with at least 1 player"))
        
        self.players[self.dealer_name] = BlackJackPlayer("Dealer", dealer=True, money=dealer_start)
        for p in players:
            if p.dealer:
                raise ValueError(self.create_except_msg("Only one dealer per game"))
            self.players[p.name] = p

        self.decks = [CardDeck() for i in range(number_of_decks)]
        self.reshuffle_threshold = reshuffle_threshold
        self.aces_high = False
        self.min_bet = float(min_bet)

    def shuffle_decks(self):
        shuffled = deque()
        for d in self.decks:
            shuffled.extend(d.cards)

        random.shuffle(shuffled)
        return shuffled

    def reshuffle(self):
        if not self.current_shuffle or len(self.current_shuffle) <= self.reshuffle_threshold:
            self.current_shuffle = self.shuffle_decks()

    def accept_bets(self):
        system("clear")
        print("Accepting Bets...\n")
        for p in self.players.values():
            if not p.dealer:
                try:
                    bet = float(input("{0} place bet (min: {1}):".format(p.name, self.min_bet)).strip())
                    if bet < self.min_bet:
                        bet = self.min_bet
                    p.bet = bet
                except ValueError:
                    p.bet = self.min_bet
            else:
                p.bet = self.min_bet
    
    def get_next_card(self):
        card = self.current_shuffle.pop()
        self.reshuffle()
        return card

    @staticmethod
    def get_card_value(card):
        return card.face_value if card.face_value <= 10 else 10

    @staticmethod
    def get_hand_value(hand):
        hand_value = 0
        aces = 0
        for c in hand:
            if str(c).startswith("ace"):
                aces += 1
            else:
                hand_value += BlackJackGame.get_card_value(c)

        for i in range(aces):
            hand_value += 1

        i = 0
        while hand_value + 10 <= 21 and i < aces:
            hand_value += 10
            i += 1

        return hand_value


    def deal_card(self, player):
        card = self.get_next_card()
        player.deal(card)


    def show_hands(self, final=False):
        if not final:
            system("clear")
        for p in self.players.values():
            p.show_hand(final=final)
        print()


    def deal_cards(self):
        for i in range(2):
            for p in self.players.values():
                self.deal_card(p)
                
        for p in self.players.values():
            print("Dealing Cards...\n")
            self.show_hands()
            if not p.dealer:
                while p.hand_value() <= 21:
                    i = input("{0} ({1}) what would you like to do? (s: stay, h: hit me!):".format(p.name, p.hand_value()))
                    if i == "s":
                        break
                    elif i == "h":
                        self.deal_card(p)
                        if p.hand_value() > 21:
                            break
                        self.show_hands()
                    else:
                        print("Invalid Input.")

        dealer = self.players[self.dealer_name]

        max_hand_value = 0
        winners = set()

        dealer_beaten = False
        for p in self.players.values():
            if not p.dealer:
                if p.hand_value() <= 21 and p.hand_value() > dealer.hand_value():
                    dealer_beaten = True
                    if p.hand_value() > max_hand_value:
                        max_hand_value = p.hand_value()
                        winners = set([p])
                    elif p.hand_value() == max_hand_value:
                        winners.add(p)


        if dealer_beaten:
            print("Dealer is beaten...!?")
            print("Dealer tries to overcome current players...")


        if dealer.hand_value() <= 17 or dealer_beaten:

            while dealer.hand_value() < max_hand_value:
                self.deal_card(dealer)
        
        if dealer.hand_value() <= 21:
            print("Yup.")
            max_hand_value = dealer.hand_value()
            winners = set([dealer])
        else:
            print("Nope.")
        

        print("\n{0} won with hand {1}.".format(list(winners), max_hand_value))
        self.show_hands(final=True)

        losers = []
        for p in self.players.values():
            if p not in winners:
                losers.append(p)

        for w in winners:
            w.collect_from(losers, len(winners))


    def show_balances(self):

        for p in self.players.values():
            print("{0} has {1}.".format(p.name, p.money))

    def reset_players(self):
        for p in self.players.values():
            p.reset_hand()


    def start(self):
        system("clear")
        self.current_shuffle = []
        while True:
            self.reset_players()
            print("Starting new game...\n")
            self.show_balances()
            play = input("Ready to play? (y/n):")
            if play == "n":
                break
            self.reshuffle()
            self.accept_bets()
            self.deal_cards()

if __name__ == "__main__":
    players = []
    names = ["JiJi", "Kevin"]
    start_money = 10000
    for n in names:
        players.append(BlackJackPlayer(n, 10000))

    game = BlackJackGame(players, number_of_decks=10, reshuffle_threshold=0, min_bet=500, dealer_start = start_money)
    game.start()

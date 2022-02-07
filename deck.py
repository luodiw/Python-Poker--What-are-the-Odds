"""
Deck of 52 cards created for shuffling and dealing.
"""

import random
import card_format as cf


def build_deck():
    """
    Create a deck of cards in 4 suits and 13 ranks.
    :return: Generated ranks and suits added to the empty deck list in the format from card_format file
    """

    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    deck = []
    for suit in suits:
        for rank in ranks:
            match = cf.create(rank, suit)
            deck.append(match)

    return deck


def shuffle_deck(my_decks):
    """
    Shuffling deck of 52 cards copying the deck cards
    :param my_decks: To be shuffled deck
    :return A shuffled deck from a randomly generated pile of cards
    """
    random.shuffle(my_decks)
    return my_decks


def deal_cards(deck_to_deal_from):
    """
    Deal deck of cards after deck is shuffled.
    :param deck_to_deal_from: Deck ready for playing
    :return: Dealt deck of cards
    """
    deck=deck_to_deal_from
    if len(deck)<5:
        deck=build_deck()

    shuffled_deck=shuffle_deck(deck)
    dealt_cards = []

    for deal in range(5):
        taken_card = random.choice(shuffled_deck)
        dealt_cards.append(taken_card)
        shuffled_deck.remove(taken_card)
    return dealt_cards, deck


if __name__ == "__main__":
    deck=build_deck()
    for x in range(12):
        _, deck=deal_cards(deck)

from copy import deepcopy

import tarotbot.cards as cards

import pytest

new_deck = lambda: deepcopy(cards.Deck(cards.tarot_deck))

#def test_deck_draw_returns_card():
#    assert type(deepcopy(cards.Deck(cards.tarot_deck)).draw()) == cards.Card

def test_deck_draw_exhausts_deck():
    deck = deepcopy(cards.Deck(cards.tarot_deck))
    with pytest.raises(IndexError):
        for c in range(79):
            deck.draw()

def test_return_returns_card():
    deck = deepcopy(cards.Deck(cards.tarot_deck))
    d_card = deck.draw()[0]
    assert not d_card in deck.curr_deck
    deck.return_card(0)
    assert d_card in deck.curr_deck

def test_draw_can_draw_several_cards():
    deck = new_deck()
    d_cards = deck.draw(3)
    assert len(d_cards) == 3
    assert type(d_cards[0]) == cards.Card

def test_list_discards():
    deck = new_deck()
    d_cards = deck.draw(3)
    assert len(deck.discards)  == 3
    assert type(deck.discards[0]) == cards.Card
    assert d_cards[0] in deck.discards

def test_remaining():
    deck = new_deck()
    deck.draw(3)
    assert deck.remaining() == 75
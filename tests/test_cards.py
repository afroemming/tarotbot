from copy import deepcopy

import tarotbot.cards as cards

import pytest

def test_deck_draw_returns_card():
    assert type(deepcopy(cards.Deck(cards.tarot_deck)).draw()) == cards.Card

def test_deck_draw_exhausts_deck():
    deck = deepcopy(cards.Deck(cards.tarot_deck))
    with pytest.raises(IndexError):
        for c in range(79):
            deck.draw()

def test_return_returns_card():
    deck = deepcopy(cards.Deck(cards.tarot_deck))
    d_card = deck.draw()
    assert not d_card in deck.curr_deck
    deck.return_card(0)
    assert d_card in deck.curr_deck
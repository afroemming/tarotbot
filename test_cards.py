import cards
import pytest

from copy import deepcopy

def test_deck_draw_returns_card():
    assert type(deepcopy(cards.tarot_deck).draw()) == cards.Card

def test_deck_draw_exhausts_deck():
    deck = deepcopy(cards.tarot_deck)
    with pytest.raises(IndexError):
        for c in range(79):
            deck.draw()

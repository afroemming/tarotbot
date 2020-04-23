# tarotbot

A simple Discord bot for drawing cards from a tarot deck.

## Usage

To start this bot, place a file named '.token' in the main program directory containing only your token, and run the file 'tarotbot.py'

## Commands

* `$draw` - Draw a single card from the deck, without replacement.
* `$reset` - Reset the deck, replacing all cards and clearing discards.
* `$remaining` - Print the number of cards left in the deck.
* `$list_discards` - Lists the names of every card in the discard deck.
* `$return_card {n}` - Return the {n}th card in the discard deck to the main deck, so that it may be drawn again.
    Note that {n} refers to the position of the card as in `$list_discards` and that it is zero indexed. 
* `$help` - print a help message to Discord.

Tarot card images from https://en.wikipedia.org/wiki/Rider-Waite_tarot_deck
from os import chdir
from sys import path

import cards

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

deck = cards.Deck(cards.tarot_deck)

#Import discord token from '.token'
chdir(path[0]) # ensure we are loading files from the directory this file is in
f = open('.token', 'r')
token = f.read()
print(f'Using token "{token}"')



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------')


@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def draw(ctx):
    """Draw a single card from the deck, without replacement."""
    try:
        drawn_card = deck.draw()[0]
        await ctx.send(f'You drew {drawn_card.name}.', file=discord.File(f'img/{drawn_card.img_name}'))
    except IndexError:
        await ctx.send('Deck is out of cards!')
    except FileNotFoundError:
        await ctx.send(f'You drew {drawn_card.name}, but I wasn\'t able to load an image!')

@bot.command()
async def remains(ctx):
    """Print the number of cards left in the deck."""
    await ctx.send(f'There are {deck.remaining()} cards remaining.')

@bot.command()
async def reset(ctx):
    """Reset the deck, replacing all cards and clearing discards."""   
    deck.reset()
    await ctx.send('All cards are back in the deck.')

@bot.command()
async def list_discards(ctx):
    """Lists the names of every card in the discard deck."""
    await ctx.send(deck.list_discards())


@bot.command(name='return')
async def _return(ctx, n: int):
    """
    Returns a card in the discard deck to the main deck, so that it may be drawn again.

    Parameters:
        n (int): Position of the card, as in `$list_discards`, to return (note: zero-indexed). 
    """
    try:
        deck.return_card(n)
        await ctx.send("Card returned!")
    except IndexError:
        await ctx.send("Error: Invalid index!")

@_return.error
async def _return_error(ctx, error):
    if isinstance(error, (commands.errors.BadArgument)):
        await ctx.send("Error parsing argument! Did you supply an int?")
    elif isinstance(error, (commands.errors.MissingRequiredArgument)):
        await ctx.send("Error: missing argument n!")
    else:
        raise error

bot.run(token)
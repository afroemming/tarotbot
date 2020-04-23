import cards

import discord

client = discord.Client()

deck = cards.Deck(cards.tarot_deck)

#Import discord token from '.token'
f = open('.token', 'r')
token = f.read()
print(f'Using token "{token}"')



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$draw'):
        try:
            drawn_card = deck.draw()
            await message.channel.send(f'You drew {drawn_card.name}.', file=discord.File(f'img/{drawn_card.img_name}'))
        except IndexError:
            await message.channel.send('Deck is out of cards!')

    if message.content.startswith('$remains'):
        await message.channel.send(f'There are {len(deck)} cards remaining.')
    
    if message.content.startswith('$reset'):
        deck.reset()
        await message.channel.send('All cards are back in the deck.')

    if message.content.startswith('$list_discards'):
        await message.channel.send(deck.list_discards())

    if message.content.startswith('$return'):
        try: 
            n = int(message.content.split()[1])
            deck.return_card(n)
            await message.channel.send("Card returned!")
        except:
            print(sys.exc_info()[0])
            await message.channel.send("Error returning card.")

    if message.content.startswith('$help'): 
        await message.channel.send(
            """

            tarotbot: A simple Discord bot for drawing cards from a tarot deck.

            The following commands are supported:
            * `$draw` - Draw a single card from the deck, without replacement.
            * `$reset` - Reset the deck, replacing all cards and clearing discards.
            * `$remaining` - Print the number of cards left in the deck.
            * `$list_discards` - Lists the names of every card in the discard deck.
            * `$return {n}` - Return the {n}th card in the discard deck to the main deck, so that it may be drawn again.
                Note that {n} refers to the position of the card as in `$list_discards` and that it is zero indexed. 
            * `$help` - print this help message.
            """
        )


client.run(token)
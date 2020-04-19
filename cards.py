from random import choice
from copy import deepcopy

class Card:
    def __init__(self, name, img_name):
        self.name = name
        self.img_name = img_name

class Deck:
    def __init__(self, cards):
        self.base_deck = deepcopy(cards)
        self.curr_deck = deepcopy(cards)

    def __len__(self):
        return len(self.base_deck)

    def remaining(self):
        return len(self.curr_deck)

    def draw(self):
        self.drawn = choice(self.curr_deck)
        self.curr_deck.remove(self.drawn)
        return self.drawn

    def reset(self):
        self.curr_deck = deepcopy(self.base_deck)


tarot_deck = [Card('Ace of Cups', 'Cups01.jpg'), Card('Two of Cups', 'Cups02.jpg'), Card('Three of Cups', 'Cups03.jpg'), 
             Card('Four of Cups', 'Cups04.jpg'), Card('Five of Cups', 'Cups05.jpg'), Card('Six of Cups', 'Cups06.jpg'), 
             Card('Seven of Cups', 'Cups07.jpg'), Card('Eight of Cups', 'Cups08.jpg'), Card('Nine of Cups', 'Cups09.jpg'), 
             Card('Ten of Cups', 'Cups10.jpg'), Card('Page of Cups', 'Cups11.jpg'), Card('Knight of Cups', 'Cups12.jpg'), 
             Card('Queen of Cups', 'Cups13.jpg'), Card('King of Cups', 'Cups14.jpg'), Card('Ace of Pentacles', 'Pents01.jpg'), 
             Card('Two of Pentacles', 'Pents02.jpg'), Card('Three of Pentacles', 'Pents03.jpg'), Card('Four of Pentacles', 'Pents04.jpg'), 
             Card('Five of Pentacles', 'Pents05.jpg'), Card('Six of Pentacles', 'Pents06.jpg'), Card('Seven of Pentacles', 'Pents07.jpg'), 
             Card('Eight of Pentacles', 'Pents08.jpg'), Card('Nine of Pentacles', 'Pents09.jpg'), Card('Ten of Pentacles', 'Pents10.jpg'), 
             Card('Page of Pentacles', 'Pents11.jpg'), Card('Knight of Pentacles', 'Pents12.jpg'), Card('Queen of Pentacles', 'Pents13.jpg'), 
             Card('King of Pentacles', 'Pents14.jpg'), Card('Ace of Wands', 'Wands01.jpg'), Card('Two of Wands', 'Wands02.jpg'), 
             Card('Three of Wands', 'Wands03.jpg'), Card('Four of Wands', 'Wands04.jpg'), Card('Five of Wands', 'Wands05.jpg'), 
             Card('Six of Wands', 'Wands06.jpg'), Card('Seven of Wands', 'Wands07.jpg'), Card('Eight of Wands', 'Wands08.jpg'), 
             Card('Nine of Wands', 'Wands09.jpg'), Card('Ten of Wands', 'Wands10.jpg'), Card('Page of Wands', 'Wands11.jpg'), 
             Card('Knight of Wands', 'Wands12.jpg'), Card('Queen of Wands', 'Wands13.jpg'), Card('King of Wands', 'Wands14.jpg'), 
             Card('Ace of Swords', 'Swords01.jpg'), Card('Two of Swords', 'Swords02.jpg'), Card('Three of Swords', 'Swords03.jpg'), 
             Card('Four of Swords', 'Swords04.jpg'), Card('Five of Swords', 'Swords05.jpg'), Card('Six of Swords', 'Swords06.jpg'), 
             Card('Seven of Swords', 'Swords07.jpg'), Card('Eight of Swords', 'Swords08.jpg'), Card('Nine of Swords', 'Swords09.jpg'), 
             Card('Ten of Swords', 'Swords10.jpg'), Card('Page of Swords', 'Swords11.jpg'), Card('Knight of Swords', 'Swords12.jpg'), 
             Card('Queen of Swords', 'Swords13.jpg'), Card('King of Swords', 'Swords14.jpg'), Card('The Fool', 'RWS_Tarot_00_The Fool.jpg'),
             Card('The Magician', 'RWS_Tarot_01_The Magician.jpg'), Card('The High Priestess', 'RWS_Tarot_02_The High Priestess.jpg'), 
             Card('The Empress', 'RWS_Tarot_03_The Empress.jpg'), Card('The Emperor', 'RWS_Tarot_04_The Emperor.jpg'), 
             Card('The Hierophant', 'RWS_Tarot_05_The Hierophant.jpg'), Card('The Lovers', 'RWS_Tarot_06_The Lovers.jpg'), 
             Card('The Chariot', 'RWS_Tarot_07_The Chariot.jpg'), Card('Strength', 'RWS_Tarot_08_Strength.jpg'), 
             Card('The Hermit', 'RWS_Tarot_09_The Hermit.jpg'), Card('Wheel of Fortune', 'RWS_Tarot_10_Wheel of Fortune.jpg'), 
             Card('Justice', 'RWS_Tarot_11_Justice.jpg'), Card('The Hanged Man', 'RWS_Tarot_12_The Hanged Man.jpg'), 
             Card('Death', 'RWS_Tarot_13_Death.jpg'), Card('Temperance', 'RWS_Tarot_14_Temperance.jpg'), Card('The Devil', 'RWS_Tarot_15_The Devil.jpg'), 
             Card('The Tower', 'RWS_Tarot_16_The Tower.jpg'), Card('The Star', 'RWS_Tarot_17_The Star.jpg'), Card('The Moon', 'RWS_Tarot_18_The Moon.jpg'), 
             Card('The Sun', 'RWS_Tarot_19_The Sun.jpg'), Card('Judgement', 'RWS_Tarot_20_Judgement.jpg'), Card('The World', 'RWS_Tarot_21_The World.jpg')]
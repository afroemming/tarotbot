"""
Generate a python file containing many tarot card objects 
"""
s = ''

# Minor Arcana
names = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',  
        'Eight', 'Nine', 'Ten', 'Page', 'Knight', 'Queen', 'King']
nums = ['01', '02', '03', '04', '05', '06', '07', '08', '09', 
    '10', '11', '12', '13', '14']

# Construct string generating a Card object (see cards.py) for each minor arcana in each suit
s = ""
for i, j in zip(names, nums):
    s +=f"Card('the {i} of Cups', 'Cups{j}.jpg'), \n"

for i, j in zip(names, nums):
    s +=f"Card('the {i} of Pentacles', 'Pents{j}.jpg '), \n"

for i, j in zip(names, nums):
    s +=f"Card('the {i} of Wands', 'Wands{j}.jpg'), \n"

for i, j in zip(names, nums):
    s +=f"Card('the {i} of Swords', 'Swords{j}.jpg'), \n"

#Major Arcana
names = ['The Fool', 'The Magician', "The High Priestess", 'The Empress',
        'The Emperor', 'The Hierophant', 'The Lovers', 'The Chariot', 
        'Strength', 'The Hermit', 'Wheel of Fortune', 'Justice', 
        'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 
        'The Star', 'The Moon', 'The Sun', 'Judgement', 'The World']
nums = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', 
    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']

for i, j in zip(names, nums):
    s +=f"Card('{i}', 'RWS_Tarot_{j}_{i}.jpg'), \n"

print(s[:-3])
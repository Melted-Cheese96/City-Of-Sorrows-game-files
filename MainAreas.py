import sys
from time import sleep
import random

def ShoppingCentreDialogue():
    print('Area not done yet')
    sleep(2)
    print('This would lead to a shopping centre, but unfortunately since this is only a one man team the area has not been developed yet. I plan to add a trading system of sorts in this area.')
    print('Restarting...')
    sleep(2)




def RandomEvent(Player):
    moneydialogue = ['You found some money in the street', 'You continue to walk']
    lucky = random.choice(moneydialogue)
    if lucky == moneydialogue[0]:
        goldAmount = random.randint(1,)
        Player.inventory['gold']


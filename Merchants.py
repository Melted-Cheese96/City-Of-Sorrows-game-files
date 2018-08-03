#In this file we have the merchants for city of sorrows text adventure shopping centre area

import sys
from time import sleep
import newcombatsystem as combat
import CityOfSorrowsV6 as mainG
import random



possibleResponses = ['Y', 'y', 'Yes', 'yes']

class ShoppingCentreMerchant:

    inventory = {'Pistol': 50,
                 'sword': 20}


    def __init__(self, name, health=100):
        self.name = name
        self.health = health


merchant1 = ShoppingCentreMerchant('Merchant')
outcome = ["Merchant: Ok, ok, I'll give you the money, just don't hurt me, please.", "Merchant: You have until the count of three to get the fuck outta my store or i'm gonna hurt you"]

def merchantScene():
        global outcome
        while True:
            print("You walk into the shopping mall, do you 'continue' or 'rob store'?")
            merchantpt1 = input()
            if merchantpt1.lower() == 'continue':

                print('Welcome to the shopping mall! We currently have this on offer: ' + str(merchant1.inventory))
                print("Do you want to purchase something?")
                purchase = input()
                if purchase.lower() in possibleResponses:
                    print('Please type in the name of what you want to buy')
                else:
                    print('Leaving shopping mall')
                    break
            elif merchantpt1.lower() == 'rob store':
                print("Player: THIS IS A STICK UP, PUT YOUR HANDS WHERE I CAN SEE THEM AND DO IT QUICK!")
                outcome1 = random.choice(outcome)
                sleep(1)
                print(outcome1)
                if outcome1 == outcome[1]:
                    combat.fightTest(mainG.PlayerName, merchant1)
                elif outcome1 == outcome[0]:
                    sleep(1)
                    print("Do you  'take all the money', or 'steal items'?")
                    merchantpt2 = input()
                    if merchantpt2.lower() == 'take all the money':
                        pass
                    elif merchantpt2.lower() == 'steal items':
                        pass
                    else:
                        print('Erorr, did you type in the wrong thing? Restarting from last checkpoint')



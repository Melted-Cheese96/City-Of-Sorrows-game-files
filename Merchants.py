#In this file we have the merchants for city of sorrows text adventure shopping centre area

import sys
from time import sleep

class ShoppingCentreMerchant:

    inventory = {'Pistol': 50,
                 'sword': 20}
    def __init__(self, name):
        self.name = name



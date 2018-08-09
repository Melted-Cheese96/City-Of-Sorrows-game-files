from time import sleep
import CityOfSorrowsV6 as mainG


possibleResponses = ['y', 'yes']




class Merchant:
    stock = {'sword': 300, 'enchanted sword': 500} #The values in this case are the prices


merchant1 = Merchant()

class Player: #Remove this class after testing
    inventory = {'gold': 500, 'Weapon': None}

    def __init__(self, health=100):
        self.health = health



def StoreType1(player):
    while True:
        merchant1 = Merchant()
        welcome = input('Welcome to the store! Would you like to buy something?')
        if welcome.lower() in possibleResponses:
            print('Here is what we currently have:')
            print(merchant1.stock)
            sleep(1)
            purchase = input('Enter the name of what you want to buy')
            if purchase.lower() == 'sword':
                print('You have chosen the sword')
                if player.inventory['gold'] >= 300:
                    print('Purchasing sword...')
                    sleep(1)
                    player.inventory['Weapon'] == 'sword'
                    player.inventory['gold'] -= 300
                    print('You have purchased the sword')
                    print('Current inventory: {}'.format(player.inventory))
                else:
                    print('Cannot afford item')
                    leave = input('Leave store?')
                    if leave.lower() in possibleresponses:
                        mainG.main()
                    elif leave.lower() == 'n' or 'no':
                        pass
            elif purchase.lower() == 'enchanted sword':
                print('You have chosen the enchanted sword!')
        elif welcome.lower() == 'no' or 'n':
            pass
        else:
            print('Error, did you type everything right?')

player1 = Player()
StoreType1(player1)
import random
from time import sleep


possibleWeapons = ['pistol', 'stick', 'sword']

damage = 0 #This variable is for the fighting function 

def NewDamage(damageTaken):
    global damage
    damage = damageTaken
    print('From function ' + str(damage))

def CheckForWep(Player):
    if Player.inventory['Weapon'] in possibleWeapons:
        print('Weapon has been found!')
        NewDamage(30)
    else:
        print('No weapon has been found!')
        NewDamage(20)

    
class Player:
    inventory = {'gold': 10, 'Weapon': 'stick'}

    def __init__(self, health=100):
        self.health = health


class Enemy:
    inventory = {}

    def __init__(self, health=100):
        self.health = health

'''
thug1 = Enemy()
player1 = Player()
'''


def fightTest(player, enemy):
    blockFate = ['Block successful', 'You have been hit']
    strike = ['You hit the enemy', 'The enemy has hit you']
    CheckForWep(player)
    print('You start fighting')
    
    while True:
        fate = random.choice(strike)
        print("Enter 'attack' to hit the enemy or 'block' to deflect the enemy")
        attack = input()
        if attack == 'attack':
            print('You try to attack the enemy')
            print(fate)
            if fate == strike[0]:
                enemy.health -= damage
                print('Damage done ' + str(damage))
                sleep(1)
                print('Their health ' + str(enemy.health))
            elif fate == strike[1]:
                player.health -= damage
                print('Damage done ' + str(damage))
                sleep(1)
                print('Current health ' + str(player.health))
        elif attack == 'block':
            print('You attempt to block the enemies attack')
            fate1 = random.choice(blockFate)
            print(fate1)
            if fate1 == blockFate[0]:
                print('No damage done to you')
            elif fate1 == blockFate[1]:
                player.health -= damage
                print('Current health ' + str(player.health))
        if player.health < 0:
            print('You die')
            break
            print('Game over, thank you for playing!')
        if enemy.health < 0:
            print('Enemy dies')
            
        



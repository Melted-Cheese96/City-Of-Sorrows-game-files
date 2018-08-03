import random
from time import sleep
import sys 

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


#This fighting system is mostly done.
def fightTest(player, enemy):
    blockFate = ['Block successful', 'Block successful', 'You have been hit'] #There are two of the same messsges to make the fighting easier for the user
    strike = ['You hit the enemy1', 'The enemy has hit you']
    CheckForWep(player)
    print('You start fighting')
    
    while True:
        fate = random.choice(strike)
        print("Enter 'attack' to hit the enemy or 'block' to deflect any of the enemys incoming attack's")
        attack = input()
        if attack == 'attack':
            print('You try to attack the enemy')
            print(fate)
            if fate == strike[0]:
                enemy.health -= damage
                #print('Damage done ' + str(damage))
                print('{} health taken from enemy'.format(str(damage)))
                sleep(1)
                print('Their health ' + str(enemy.health))
            elif fate == strike[1]:
                player.health -= damage
                print('{} health taken from you'.format(str(damage)))
                sleep(1)
                print('Your Current health ' + str(player.health))
        elif attack == 'block':
            print('You attempt to block the enemies attack')
            fate1 = random.choice(blockFate)
            print(fate1)
            if fate1 == blockFate[0]:
                print('No damage done to you')
                print('Current health ' + str(player.health))
            elif fate1 == blockFate[1]:
                print('No damage done to you')
                print('Current health ' + str(player.health))
            elif fate1 == blockFate[2]:
                player.health -= damage
                print('Current health ' + str(player.health))
        if player.health < 0 or player.health == 0:
            print('You die')
            print('Game over, thank you for playing!')
            sys.exit()
        if enemy.health < 0:
            print('Enemy dies')
            break


#fightTest(player1, thug1)


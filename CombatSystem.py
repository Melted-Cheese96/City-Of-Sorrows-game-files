from time import sleep
import random 
import sys

#OLD COMBAT SYSTEM

damage = 0

possibleWeapons = ['Pistol', 'stick', 'axe']


def damage(DamageDealt):
    global damage
    DamageDealt = damage

def damageTaken(healthTaken, character):
    healthTaken -= character.health 






def Fight(player, enemy, damage=20): #Proper fight system

    if player.inventory['Weapon'] == possibleWeapons[1]:
        print('You have a stick in your inventory!')
        damage = 30
    else:
        pass
    strike = ['You strike the enemy', 'You are hit by the enemy']
    print('You start fighting the enemy.')
    enemyAlive = True
    while enemyAlive == True :
        fate = random.choice(strike) #CHANGE BACK
        sleep(1)
        print(fate)
        if fate == strike[0]:
            enemy.health -= damage
            print('Enemies health ' + str(enemy.health))
            sleep(1)
            print('Damage done ' + str(damage))
            sleep(1)
            if enemy.health < 5:
                print('Enemy is on low health')
                sleep(1)
                print('Finish enemy off?')
                finish = input()
                if finish == 'yes':
                    print("Do you 'stomp on their face' or 'kick them a bit'?")
                    finishpt2 = input()
                    if finishpt2.lower() == 'stomp on their face':
                        print('You stonp on their face, what a cruel heartless bastard you are')
                        enemyAlive = False
                    elif finishpt2.lower() == 'kick them a bit':
                        print('You kick them around, as you do you can hear sirens in the background...')
                        sleep(1)
                        enemyAlive = False
                    else:
                        print('Error, did you type everything right?')
                elif finish == 'no':
                    pass
        elif fate == strike[1]:
            player.health -= damage
            print('Your health: ' + str(player.health))
            sleep(1)
            print('Damage done ' + str(damage))
            sleep(1)
            if player.health < 0:
                print('Darkness starts coming towards you')
                sleep(1)
                print('Everything around you fades...')
                sleep(1)
                print('You die....')
                sys.exit()
        



class Player:

    inventory = {'weapon': None, 'gold': 0}

    def __init__(self, health=100):
        self.health = health



class Thug:

    inventory = {'Weapon': None, 'gold': 10}

    def __init__(self, health=100):
        self.health = 100

'''
thug1 = Thug()
player1 = Player()

Fight(player1, thug1)
'''

if __name__ == '__main__':
    pass
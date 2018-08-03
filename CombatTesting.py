import random
import sys
from time import sleep


#Testing 23543ew463456


def CheckForWep(Player):
    weaponornot = False
    if Player.inventory['Weapon'] != None:
        print('You have a weapon')
        weaponornot = True
    else:
        print('You do have a weapon')


class Player:
    def __init__(self, health=100, damage=0, name='Player'):
        self.health = health
        self.damage = damage
        self.name = name

    inventory = {'Weapon': 'stick'}



class EnemyType1:
    def __init__(self, health=100, damage=0, name='Low level thug'):
        self.health = health
        self.damage = 10
        self.name = name



def FightOld(Player1, Enemy):
    print("'player' is now fighting with 'enemy'")
    outcome = ['You win the fight', 'you lose the fight']
    strike = ['You have struck the enemy', 'the enemy has hit you']
    for hits in range(10):
        fate = random.choice(strike)
        if fate == strike[0]:
            print('You have struck the enemy')
            EnemyDefeated = False
            while EnemyDefeated == False:
                print('Strike test')
                Enemy.health -=5
                print(Enemy.health)
                sleep(1)
                if Enemy.health < 5:
                    print('Enemy is on critical health, finish?')
                    finish = input()
                    if finish == 'yes':
                        print('You slay the enemy')
                        break
                    elif finish == 'no':
                        break
                        print('You leave the enemy there')
                else:
                    pass
        elif fate == strike[1]:
            print('The enemy has struck you')


def Fight(Player1, Enemy): #Fight for the tavern fight
    strike = ['You have struck the enemy with your weapon', 'the enemy has hit you']
    enemyAlive = True
    print('To this point')
    while enemyAlive == True:
        fate = random.choice(strike)
        if fate == strike[0]:
            Enemy.health -=10
            print('You have hit the enemy')
            sleep(2)
            print('Enemies health: ' + str(Enemy.health))
            sleep(2)
        elif fate == strike[1]:
            Player1.health -=10
            print('The enemy has hit you')
            sleep(2)
            print('Your health: ' + str(Player1.health))
            sleep(2)
            if Player1.health == 0:
                print('You die, game over')
                sys.exit()
            elif Enemy.health < 5 or Enemy.health == 0:
                print('The enemy is on critical health, finish off?')
                finish = input()
                if finish == 'yes':
                    enemyAlive = False
                    print('You chose yes')
                    break
                elif finish == 'no':
                    print('You chose no')
                    break
                else:
                    print('Error')
                    sys.exit()


def GunFightHouse(Player1, Enemy):
    strike = ['You have shot the enemy', 'the enemy has hit you with their sword ']
    enemyAlive = True
    print('You start fighting....')
    while enemyAlive == True:
        fate = random.choice(strike)
        if fate == strike[0]:
            Enemy.health -= 30
            print('You have shot the enemy')
            sleep(2)
            print('Enemies health: ' + str(Enemy.health))
            sleep(2)
        elif fate == strike[1]:
            Player1.health -= 20
            print('The enemy has hit you')
            sleep(2)
            print('Your health: ' + str(Player1.health))
            sleep(2)
            if Player1.health == 0:
                print('You fall to the ground...')
                sleep(1)
                print('Things start fading to black....')
                sleep(2)
                print('You are dead')
                sleep(1)
                print('Game over')
                sys.exit()
            elif Enemy.health < 0:
                print('The enemy is on critical health, finish off?')
                finish = input()
                if finish == 'yes':
                    enemyAlive = False
                    print('You chose yes')
                    break
                elif finish == 'no':
                    print('You chose no')
                    break
                else:
                    print('Error')
                    sys.exit()

player1 = Player()
thug = EnemyType1()

#Fight(player1, thug)


if __name__ == '__main__':
    pass
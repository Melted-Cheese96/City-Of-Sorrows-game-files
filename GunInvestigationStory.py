import sys
from time import sleep


def GunInvestigation(Player):  # Not finished, continue! This function gets called when you get to your home after losing the tavern fight. It can also happen when you win the tavern fight.
    print('Checkpoint reached...')
    while True:
        print('You start walking to your home...')
        sleep(1)
        print('You arrive at your home')
        sleep(1)
        print("You find a pistol that has recently been discharged, do you 'pick up' or 'investigate'?")
        answer = input()
        if answer.lower() == 'pick up':
            print('Picking up pistol')
            print('Pistol acquired')
            Player.inventory['Weapon'] = 'Pistol'
            print(Player.inventory)
            print(Player.damage['Pistol'])
            sleep(2)
            print('Dun...')
            sleep(1)
            print('Dun...')
            sleep(2)
            print('You see two people in your house stuffing something into the fridge')
            print("Do you 'try to shoot them' or 'run away'?")
            attackornot = input()
            sleep(2)
            if attackornot.lower() == 'try to shoot them':
                pass
            elif attackornot.lower() == 'run away':
                pass
            else:
                print('Error, did you type something wrong? Restarting from last checkpoint...')

        elif answer == 'investigate':
            print('You start investigating')
            sleep(2)
            print('You see blood around your house')

        else:
            print('Error, have you entered everything correctly? Restarting from last checkpoint...')





GunInvestigation()


if __name__ == '__main__':
    pass
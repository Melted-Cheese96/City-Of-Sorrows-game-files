import sys
from time import sleep
import random
import CombatTesting as ct




def GunInvestigation(player):
    print('Checkpoint reached...')
    calmOutcome = ['They run out of your house, leaving the fridge open', 'They run towards you']
    Shootoutcome = ['You shoot both of the intruders with your pistol', 'You miss your shot and the intruders are alerted of your position']
    Runoutcome = ['You run as fast away as you can from the intruders', 'The intruders hear you running away and start chasing after you.']
    outcome2 = random.choice(Runoutcome)
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
            player.inventory['Weapon'] = 'Pistol'
            print(player.inventory)
            sleep(2)
            print('Dun...')
            sleep(1)
            print('Dun...')
            sleep(2)
            print('You see two people in your house stuffing something into the fridge')
            print("Do you 'try to shoot them' or 'run away'?")
            attackornot = input()
            sleep(2)
            while True:
                print('Checkpoint reached')
                if attackornot.lower() == 'try to shoot them':
                    sleep(1)
                    print('You start pointing the gun at the intruders')
                    outcome = random.choice(Shootoutcome)
                    sleep(1)
                    print(outcome)
                    if outcome == Shootoutcome[0]: #Continue this
                        print('The intruders fall to the ground and seem to be bleeding out....')
                        sleep(1)
                        break
                    elif outcome == Shootoutcome[1]:
                        print("The intruders start coming after you, do you 'fight' or 'play it calm'")
                        fightoption = input()
                        if fightoption.lower() == 'fight':
                            ct.GunFightHouse(player1, intruder1)
                        elif fightoption.lower() == 'play it calm':
                            print('You wait for the intruders...') #UIOHWRETGUIHERGIHUGRHIO
                            sleep(1)
                            result = random.choice(calmOutcome)
                            print(result)
                            sleep(1)
                            if result == calmOutcome[0]:
                                print("Do you 'check the fridge' or 'get outta there'")
                                questpt4 = input()
                                if questpt4.lower() == 'check the fridge':
                                    print('You start walking over to the fridge....')
                                    sleep(1)
                                    print('You see a dead decomposing body in the fridge!')
                                    sleep(1)
                                    print('You hear sirens in the background...')
                                    sleep(1)
                                    print("Do you 'run away' or 'dispose of the body'?")
                                    questpt5 = input()
                                    if questpt5.lower() == 'run away':
                                        pass
                                    elif questpt5.lower() == 'dispose of the body':
                                        pass
                                    else:
                                        print('Error, did you type everything right?')
                            elif result == calmOutcome[1]:
                                print('From option 1')
                            else:
                                print('Error, restarting....')
                        else:
                            print('Error, did you spell everything right?')
                elif attackornot.lower() == 'run away':
                    print('You start to run away...')
                    print(outcome2)
                    if outcome2 == Runoutcome[0]:
                        print('You find yourself in another street that you have not been to before, you see an open sewer grate.')
                        sleep(1)
                        print('The intruders are getting closer')
                        print('Go inside the open sewer grate?')
                        sewers = input()
                        if sewers == 'yes':
                            print('You run over to the sewer grate')
                            sleep(1)
                            print('You lower yourself into the opening')
                            sleep(1)
                            print('You crawl through the tunnel, it is covered in shit')
                        elif sewers == 'no':
                            print('You continue to run down the street')
                            sleep(1)
                            print('You trip.....')

                    elif outcome2 == Runoutcome[1]: #Continue
                        print('From option 2')
                else:
                    print('Error, did you type something wrong? Restarting from last checkpoint...')

        elif answer == 'investigate':
            print('You start investigating')
            sleep(2)
            print('You see blood around your house')

        else:
            print('Error, have you entered everything correctly? Restarting from last checkpoint...')

class Intruders:
    inventory = {'Weapon': 'Sword'}
    weaponDamage = {'Sword': 20}
    health = 100


    def __init__(self, name):
        self.name = name

intruder1 = Intruders('Intruder1')
intruder2 = Intruders('Intruder2')

class Player:

    weaponDamage = {'Pistol': 30}
    inventory = {'Weapon': None}
    health = 100


    def __init__(self,name):
        self.name = name

player1 = Player('player1')



GunInvestigation(player1)



if __name__ == '__main__':
    pass
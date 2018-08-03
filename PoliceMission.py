import random
from time import sleep


class Player:
    inventory = {'gold': 10, 'Weapon': 'stick'}

    def __init__(self, health=100):
        self.health = health

player1 = Player()

def LeftTunnel(Player):
    while True:
        print('The tunnel seems to drop off down a hole')
        sleep(1)
        print('You can hear the police above so you decide to jump down the hole')
        sleep(1)
        print('THUD!!')
        sleep(1)
        print('You hit the bottom of this hole and you can hardly see what is there')
        print("However, you can hear running water, there seems to be another tunnel, do you go through that tunne;?")
        tunnelpt1 = input()
        if tunnelpt1 == 'yes':
            print('You enter the tunnel')
            sleep(1)
        elif tunnelpt1 == 'no':
            print('You decide not to go there, all of a sudden the floor starts opening')
            sleep(1)
            print('You fall down....')
            sleep(1)
            print('A few hours later....')
            sleep(1)
            print('It seems that you landed in a dungeon of sorts')
            sleep(1)
            print('The air smells really rank')
            sleep(1)
            print("You are near a table, on the table is a sword and a pistol, which one do you take?")
            sleep(1)
            tunnelpt2 = input()
            if tunnelpt2.lower() == 'sword':
                print('You pick up the sword')
                player.inventory['Weapon'] = 'sword'
                print('Current inventory' + player.inventory['Weapon'])
            elif tunnelpt2.lower() == 'pistol':
                print('You pick up the pistol')
                player.inventory['Weapon'] = 'pistol'
                print('Current inventory ' + player.inventory['Weapon'])
            else:
                print('Error, did you type everything right?')
    else:
        print('Error, did you type everything right?')


def RightTunnel(Player):
    while True:
        print('Checkpoint reached...')

        print('You seem to be approaching a turn in the tunne;')
        sleep(1)
        print("Do you 'take the turn' or 'keep going'?")
        rightTunnelpt1 = input()
        if rightTunnelpt1.lower() == 'take the turn':
            print('You through around the turn')
            sleep(1)
            print('You see light coming from the outside...')
            sleep(1)
            print('It seems that you had been down in the tunnels for longer than you had thought....')
            sleep(1)
            print('You come out of the tunnels near a river of sorts')
            sleep(1)
            print("Do you 'go back to the town centre' or 'go down the river'?")
            rightTunnelpt2 = input()
            if rightTunnelpt2.lower() == 'go back to the town centre':
                print('You start walking back to the town centre....')
                #GET MAIN AREA FUNCTION FROM MAIN GAME
            elif rightTunnelpt2.lower() == 'go down the river':
                pass
            else:
                print('Error, did you type everything right? Restarting from last checkpoint.')

        elif righTunnelpt1.lower() == 'keep going':
            print('You continue to go straight....')
            sleep(1)
        else:
            print('Error, did you type everything right? Restarting from last checkpoint')

def east(): #This is for when you go east on the bike
    pass

def north(): #This is for when you go north on the bike
    print('You can hear the police cruisers right behind you...')
    sleep(1)
    print('You start riding through the residential area')

def west(): #This is for when you go west on the bike
    pass

def south(): #This is for when you go south on the  bike
    pass


def PoliceMissionPt1(player): #This is for after the tavern fight
    while True:
        print("You have blood all over your face at this point from the fight. Thing's aren't looking good for you if you were to get caught")
        sleep(1)
        print("Do you either, 'flee the scene' or 'hide nearby'?")
        policemissionpt1 = input()
        if policemissionpt1.lower() == 'flee the scene':
            print('You start running away')
            sleep(1)
            print("You see a bike in a parking lot nearby, do you 'hijack bike' or 'continue running'?")
            fleept1 = input()
            if fleept1.lower() == 'hijack bike':
                print('You run over to the bike')
                sleep(1)
                print('Checkpoint reached')
                print('You are now on the bike')
                sleep(1)
                print("Do you go 'east', 'north', 'west', or 'south'")
                bikept1 = input()
                if bikept1.lower() == 'east':
                    print('You start cycling east')
                    east()
                elif bikept1.lower() == 'north':
                    print('You start cycling north')
                    north()
                elif bikept1.lower() == 'west':
                    print('You start cycling west')
                    west()
                elif bikept1.lower() == 'south':
                    print('You start cycling south')
                    south()
                else:
                    print('Error, did you type everything right? Restaring from last checkpoint')
            elif fleept1.lower() == 'continue running':
                print('You continue running')
            else:
                print('Error, did you type everything right? Restarting from last checkpoint')
        elif policemissionpt1.lower() == 'hide nearby':
            print("There is a dumster nearby, do you 'hide in dumpster' or 'hide in the nearby sewer grate'?")
            policemissionpt2 = input()
            if policemissionpt2 == 'hide in dunpster':
                print('You start walking over the dumpster...')
                sleep(1)
                print('You get in the dumpster')
                sleep(1)
                print('You can hear the police talking in the background')
                print('They do not seem to take any note of the dumpster')
                sleep(1)
            elif policemissionpt2 == 'hide in the nearby sewer grate':
                print('You struggle to open the sewer grate')
                sleep(1)
                print('You finally get the grate open')
                print('The police are getting close to your location....')
                print('The chances of the police getting to you are quite high')
                sleep(1)
                print("Do you 'jump into the sewer' or 'run'")
                policemissionpt3 = input()
                if policemissionpt3.lower() == 'jump into the sewer':
                    print('You jump into the sewer, your shoes hit the floor with a THUD')
                    sleep(1)
                    print('Do you go through the tunnel on the left or on the right')
                    policemissionpt4 = input()
                    if policemissionpt4.lower() == 'left':
                        print('You climb through the tunnel on the left...')
                        LeftTunnel(player1)
                    elif policemissionpt4.lower() == 'right':
                        print('You climb through the tunnel on the right...')
                        sleep(1)
                    else:
                        print('Error, did you type everything right?')
                elif policemissionpt3.lower() == 'run':
                    pass
                else:
                    print('Error, did you type everything right?')
            else:
                print('Error, did you type everything right?')
        else:
            print('Error, did you type everything right?')


if __name__ == '__main__':
    pass

import random
from time import sleep


def LeftTunnel(Player):
    pass

def RightTunnel(Player):
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
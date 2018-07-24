import random
from time import sleep
import sys
import CombatTesting as ct
import MainAreas as ma
import GunInvestigationStory as guni



#
# Version 10.06



possibleWeapons = {'Pistol': 'pistol', 'Stick': 'stick',
                   'Sword': 'sword'}  # These are the weapons that are currently available


def AddMoney(playername, amount=0):  # gold system
    playername.inventory['gold'] += amount
    print('You have recieved money, you now have ' + str(playername.inventory['gold']) + ' gold')


def RemoveMoney(playername, amount=0):  # Remove Gold system
    playername.inventory['gold'] -= amount
    print('Lost money, you now have ' + str(playername.inventory['gold']))


class FirstClassThug:  # Easiest thug.
    inventory = {'gold': 200, 'Weapon': None}
    health = 100

    def __init__(self, health=100):
        self.health = 100


thug = FirstClassThug()


class weaponStick:
    damage = {'stick': 10}  # Damage for the stick.


stick = weaponStick()


class Player:  # Class for the player.
    inventory = {'gold': 10, 'Weapon': None, 'Misc': None}
    health = 100

    def __init__(self, health=100, inventory='inven'):
        self.health = 100
        self.inventory = {'gold': 10, 'Weapon': None, 'Misc': None}


def getWep():
    global PlayerName
    PlayerName.inventory['Weapon'] = 'stick'
    print(PlayerName.inventory)
    print('Weapon acquired')


def TavernQuestDrink():  # Continue story line, this function gets triggered when you choose the have a drink option in the tavern section of the program.
    while True:
        print('You have ordered a beer...')
        sleep(2)
        print('You recieve your beer...')
        sleep(2)
        print('You take a sip')
        sleep(2)
        print('The drink tastes a litte strange...')
        print('You notice someone intently watching you from the corner of the tavern')
        sleep(1)
        print("Do you 'confront' or 'walk away'?")
        tavquest1 = input()
        if tavquest1 == 'confront':  # Story line when you confront the person
            print('You start walking over to the person')
            sleep(1)
            print('Before you get over there, you start feeling really light headed. You eventually pass out')
            print(PlayerName.inventory)  # Continue this!!
        elif tavquest1.lower() == 'walk away':
            print('You start walking away...')  # Finish!!!!!
            sleep(2)
            print('You get out of the tavern')
            guni.GunInvestigation(PlayerName)
        else:
            print('Error, restarting from last checkpoint, did you spell your answer correctly?')

'''
def GunInvestigation(): #Working on this in another file
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
            PlayerName.inventory['Weapon'] = 'Pistol'
            print(PlayerName.inventory)
            print(PlayerName.damage['Pistol'])
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
'''

def option2story():  # This function gets called after you lose the tavern fight. PROPER STORYLINE.
    while True:
        print("You wake up on the cold hard floor, do you 'look for the thugs' or 'go home'")
        choice = input()
        if choice.lower() == 'look for the thugs':
            print('You swiftly jump up, it seems that you were out the whole night. The sun is rising')
            print("Do you go 'left' or 'right'?")
            choice2 = input()
            if choice2.lower() == 'left':  # Finish!
                print('You went left')
                sleep(1)
                print("You see people that are bothering someone else, do you 'confront' or 'keep looking', or give up and 'go to town square'?")
                choice3 = input()
                if choice3 == 'confront':  # Story-line when you confront them
                    option2storyconfront()
                elif choice3.lower() == 'keep looking':
                    print('Test2')
                else:
                    print('Error')
            elif choice2.lower() == 'right':  # Finish!
                print('You went right')
                sleep(1)
                print('')
            elif choice2.lower() == 'go to town square':
                print('You start walking back to the main part of town')
                sleep(2)
                print("Do you go to the 'tavern' or 'shopping centre'?")
                townsquare = input()
                if townsquare.lower() == 'tavern':
                    Tavern()

            else:
                print('Wrong entry, try again')
        elif choice.lower() == 'go home':  # The rest of the code for this section is in the GunInvestigation function
            GunInvestigation()


def homeortav():  # This function ties into the tavern storyline, this function gets called after you win the tavern fight.
    print('Checkpoint reached...')
    sleep(1)
    while True:
        print('You have won the fight')
        sleep(1)
        print("You decide to go home just in case any more thugs come your way")
        sleep(1)
        GunInvestigation()



def FireScene():  # Ties into the fire scene from the WalkAwayOption function. NOTE: FINISHED
    print('Checkpoint reached...')
    while True:
        fire = input()
        if fire == 'walk through the flames':
            print('You try walking through the flames but you get burnt.')
            sleep(1)
            print('The flames start coming closer...')
            sleep(2)
            print('You hear the fire department coming to your area but it\'s too late at this point')
            sleep(1)
            print('You start fading away from this world...')
            sleep(3)
            print('You die from serious burns')
            sleep(1)
            print('Game over...')
            sys.exit()
        elif fire == 'climb out the window':
            print('The thugs glued the window shut while you were asleep')
            print('The flames start coming closer...')
            sleep(1)
            print('You hear the fire department coming to your area but it\'s too late at this point')
            sleep(1)
            print('You start fading away from this world...')
            sleep(3)
            print('You died from serious burns')
            sleep(1)
            print('Game over...')
            sys.exit()
        else:
            print('Wrong answer, restarting from last checkpoint...')


def WalkAwayOption():  # Function gets called after you walk away from the fight in the tavern fight scene. NOTE: FINISHED
    print('You start walking away...')
    sleep(2)
    print('After twenty minutes you assume the thugs are gone')
    sleep(1)
    print('You arrive at your home...')
    sleep(1)
    print('You go straight to bed')
    sleep(5)
    print('Smash!...')
    sleep(2)
    print('*Muffled laughter')
    sleep(1)
    print('The thugs from the tavern are back!')
    sleep(1)
    print('There is a fire coming from your living room in the house')
    sleep(1)
    print('The fire is coming closer and you start to cough')
    sleep(1)
    print('The fire comes too close, the fire dept are on their way but you have no way to get out')
    print("Do you 'walk through the flames' or 'climb out the window'?")
    FireScene()


def TavernQuestFight():  # This function gets called once you leave the tavern. NOTE: THIS FUNCTION IS FINISHED
    print('Leaving tavern...')
    sleep(2)
    print('From TavernQuestFight')
    #ct.CheckForWep(PlayerName)
    sleep(2)
    print('As you step outside of the tavern you get approached by a group of mean looking thugs...')
    sleep(1)
    print('The thugs are starting to push you around, they are obviously looking for a fight')
    sleep(1)
    print("Do you 'fight' or 'walk away'")

    fight = input()
    if fight.lower() == 'fight':  # Continue the rest
        print(fate)
        fateoption0()
    elif fight.lower() == 'walk away':
        WalkAwayOption()


BallQuestFight = ['You win the fight', 'You lose the fight']


def BallQuestSewers():
    print('You enter the muddy sewers')
    sleep(1)
    print('You see a bunch of graffiti on the walls of the sewer.')
    print('There are two ways that you can go.')
    print('You hear a cry of help coming from the left side')
    sleep(2)
    print("Do you 'follow the cries' or 'go the other path'?")
    ballquestsewerspt1 = input()
    if ballquestsewerspt1 == 'follow the cries':
        print('You start walking closer to the person')
        sleep(2)
        print('after about 5 minutes of walking you hear the screams start to faint and you hear laughter')
        sleep(2)
        print('You start running, somehow though the ground opens up and you fall inside this chamber of sorts')
        sleep(2)
        print('A bat goes across your head and you pass out')
        sleep(2)
        print('...')
        sleep(2)
        print('...')
        sleep(1)
        print('...')
        sleep(2)
        print('You wake up')
        sleep(2)
        print('It seems that someone has tied you up to a chair')
        sleep(2)
        print('The walls are bloody, ')
        sleep(1)
        while True:
            print('Checkpoint reached...')
            sleep(2)
            print("You are tied up with rope, do you 'try to break rope' or 'pretend to sleep'?")
            ballquestpt2 = input()
            if ballquestpt2 == 'try to break rope':
                print('You try to break the rope that is holding you, unfortunately the rope is very right. You cannot seem to break it')
            elif ballquestpt2 == 'pretend to sleep':
                print('You pretend to sleep for several hours...')
                sleep(2)
                print('You suddenly hear a very familiar voice, it is the little boy from the park who had lost his ball')
                sleep(2)
                print('The boy is laughing heavily')
                sleep(2)
                print('The little boy comes it and stabs you in the stomach with a knife')
                PlayerName.health = 30
                sleep(2)
                print('Your health: ' + str(PlayerName.health))
                sleep(2)
                print('You yelp in pain')
                Boy = Child()
                print('Child\'s health ' + Boy.health)
                sleep(2)
                print('He is about to stab you again')
                sleep(2)
                print("Do you 'try to kick him in the face' or protect stomach with legs'?")
                ballquestpt3 = input()
                if ballquestpt3 == 'try to kick him in the face':
                    print('You manage to kick the boy in the face but his other thugs start flooding the room')
                    sleep(2)
                elif ballquestpt3 == 'protect stomach with legs':
                    print('You try to protect your stomach with your legs and he ends up stabbing your leg')
                    sleep(2)
                    print('It hurts')
                    sleep(2)
                    PlayerName.health = 20

            else:
                print('Error restarting from last checkpoint')
    elif ballquestsewerspt1.lower() == 'go the other path':
        print('You decide to stay on the safe side and take the right side')
        sleep(2)
        print('There is blood on the walls')
        sleep(1)
        print('Wrong choice much?')
    else:
        print('Error, restarting from last checkpoint')


def BallQuestParkPt2():  # This function is called when you go right after staying back. This is an extension of the BallQuestPark function.
    while True:
        print('Checkpoint reached')
        sleep(2)
        print("You find the ball, the ball is near the sewers. do you 'look inside the sewers' or 'pick up the ball'?")
        ballquestpt3 = input()
        if ballquestpt3.lower() == 'look inside the sewers':
            print('You start walking into the sewers')
            BallQuestSewers()
        elif ballquestpt3.lower() == 'pick up the ball':
            print('You pick up the ball')
            PlayerName.inventory['Misc'] = 'Ball'
            print("Do you 'keep ball' or 'give ball back'?")
            ballquestpt4 = input()
            if ballquestpt4.lower() == 'keep ball':
                print('You keep the ball and head back to your home')
            elif ballquestpt4.lower() == 'give ball':
                print('You walk back to the child')
                sleep(2)
                print('You give the ball back to the child')
                PlayerName.inventory['Misc'] = None
                print(PlayerName.inventory)
            else:
                print('Error, are you sure that you typed everything correctly? Restarting from last checkpoint...')
        else:
            print('Error restarting from last checkpoint')


def BallQuestPark():  # This function ties into the park storyline. NOTE: THIS FUNCTION IS STILL NOT COMPLETELY FINISHED

    print('Checkpoint reached...')
    print('You arrive at the park, a little boy wants help finding his ball')
    while True:
        print("Do you look 'left' or 'right'?")
        BallQuest1 = input()
        if BallQuest1 == 'left':
            print('You look left but don\'t see the ball')
            sleep(1)
            print('Try again')
        elif BallQuest1 == 'right':
            print("You see something to your right, do you 'follow' or 'stay back'?")
            BallQuest2 = input()
            if BallQuest2 == 'stay back':
                while True:
                    print("You stay back, do you look 'left', 'right', or 'foward'?")
                    BallQuest1 = input()
                    if BallQuest1.lower() == 'left':
                        print('You look left')
                        print('You do not see the ball')
                    elif BallQuest1.lower() == 'right':
                        print('You look right')
                        sleep(2)
                        print('You see a red ball near the sewers...')
                        sleep(1)
                        print('You go towards it')
                        sleep(1)
                        BallQuestParkPt2()
            elif BallQuest1.lower() == 'forward':
                print('You looked forward')
            elif BallQuest2 == 'follow':
                print("You decide to follow this thing, you follow this thing into the dirty, muddy sewers.")
                print('You start walking towards the sewers...')
                sleep(2)
                print('You enter the sewers...')
                sleep(1)
                print('Dun...')
                sleep(1)
                print('Dun...')
                print('You hear something coming towards you!')
                sleep(1)
                print("You run into a thug that is unarmed.")
                print("Do you either 'run', or 'fight'?")
                fight = input()
                if fight == 'fight':
                    ct.Fight(Player1, Enemy1)
                elif fight == 'run':  # CONTINUE
                    print('You run')
        elif BallQuest1.lower() == ' forward':
            print('You look forward, but do not see the red ball')



class Child:
    health = 50
    inventory = {'Weapon': 'knife'}

    def __init__(self, health=50, inventory=inventory):
        self.health = health




# The following two lines are for the tavern fight


def Tavern():
    print('Entering tavern...')
    sleep(3)
    print("You enter the tavern, do you 'order a drink', or 'leave' you notice there is also a stick near the door, do you 'pick up the stick'?")
    tavQues = input()
    if tavQues.lower() == 'leave':
        TavernQuestFight()
    elif tavQues.lower() == 'order a drink':
        TavernQuestDrink()
    elif tavQues.lower() == 'pick up the stick':
        print('You walk over to the stick...')
        sleep(2)
        print('You pick up the stick')
        PlayerName.inventory['Weapon'] = 'stick'
        print('Current inventory' + str(PlayerName.inventory))
        sleep(2)
        print("Do you 'go outside' or 'order a drink'")
        tavQues2 = input()
        if tavQues2.lower() == 'go outside':
            tavquesPath3()
        elif tavQues2.lower() == 'order a drink':
            TavernQuestDrink()
        else:
            print('Error, restarting from last checkpoint')


def tavquesPath3():  # New combat system in play.
    print('You walk outside...')
    sleep(2)
    print('You step outside the tavern, there are some thugs that are starting to bother you')
    sleep(2)
    print("It is clear that these thugs want a fight, do you 'fight' or 'walk away'?")
    tavQues4 = input()
    if tavQues4 == 'fight':
        print('You decide to fight')
        print('Checkpoint reached')
        sleep(1)
        ct.Fight(PlayerName, thug)
    elif tavQues4 == 'walk away':
        WalkAwayOption()
    else:
        print('Error restarting from last checkpoint')

def Backstory(filename, start): #This is supposed to be only for the back story but I got really lazy so it's just this
    story = open(filename, 'r')
    print(story.read())
    sleep(1)
    if start == 'yes':

        print('Starting game...')
    else:
        pass
    sleep(2)


PlayerName = Player()
while True:
    print('Before we start here are some things that you should know:')
    Backstory('Quick tips', '')
    print('Welcome to the City Of Sorrows! Do you want to get the backstory?')
    backstory = input()
    if backstory == 'yes':
        Backstory('City of sorrows lore', 'yes')
    elif backstory == 'no':
        pass
    else:
        print('Error')
    print('As you enter the main areas of the City Of Sorrows you notice there are a few places where you can go that are open.')
        # print('You are equipped with a stick to start off')
        # getWep()
    print("You see a 'tavern', a 'shopping centre' and a 'park', where do you go?")
    answer1 = input()
    if answer1.lower() == 'tavern':  # Tavern story line
        Tavern()
    elif answer1.lower() == 'shopping centre':
        ma.ShoppingCentreDialogue()
    elif answer1.lower() == 'park':
        print('You walk to the park...')
        sleep(2)
        BallQuestPark()
    else:
        print('Error, wrong selection')



from time import sleep
import CombatTesting as ct




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
                print(
                    'You try to break the rope that is holding you, unfortunately the rope is very right. You cannot seem to break it')
            elif ballquestpt2 == 'pretend to sleep':
                print('You pretend to sleep for several hours...')
                sleep(2)
                print(
                    'You suddenly hear a very familiar voice, it is the little boy from the park who had lost his ball')
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
                    ct.FightTesting(Player1, Enemy1)
                elif fight == 'run':  # CONTINUE
                    print('You run')
        elif BallQuest1.lower() == ' forward':
            print('You look forward, but do not see the red ball')


if __name__ == '__main__':
    pass
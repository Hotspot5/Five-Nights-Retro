import threading
import time
import random
import constants

def cls():
    print("\033[H\033[2J\033[3J", end="")

MOVEMENT_FREQ = constants.MOVEMENT_FREQ
NIGHT_LEN = constants.NIGHT_LEN
ANIMATRONIC_GAP = constants.ANIMATRONIC_GAP

FPS = constants.FPS

AI_LEVELS = constants.AI_LEVELS

status = {
    'freddy': 0, 
    'bonnie': 0, 
    'chica': 0, 
    'foxy': 0, 
    't freddy': 0, 
    't bonnie': 0, 
    't chica': 0, 
    'w freddy': 0, 
    'w bonnie': 0, 
    'w chica': 0, 
    'w foxy': 0, 
    'bb': 0, 
    'mangle': 0, 
    'springtrap': 0, 
    'itsme': 0, 
}

nightTimer = 0

leftDoorDown = 0
rightDoorDown = 0
maskOn = 0
foxyFlashed = 0
puppetTimer = 0

def gameloop():
    global nightTimer, status
    
    start = time.time()
    
    while nightTimer < NIGHT_LEN:
        
        while time.time() - start < MOVEMENT_FREQ:
            time.sleep(1/FPS)
            
        start = time.time()
        nightTimer += MOVEMENT_FREQ
        
        for animatronic in status:
            if random.random() < AI_LEVELS[animatronic] / 20:
                 status[animatronic] += 1
                 #print(animatronic, status[animatronic])
            time.sleep(ANIMATRONIC_GAP)
    return
        
threading.Thread(target=gameloop).start()

location = 'center'

while True:
    
    cls()
    
    if location == 'center':
        print('Where do you want to go?\n\n1 - Left Door\n2 - Left Vent\n3 - Hallway\n4 - Right Door\n5 - Right Vent\n6 - Parts and Service')
        choice = input('\n> ')
        if '1' in choice:
            location = 'l door'
        elif '2' in choice:
            location = 'l vent'
        elif '3' in choice:
            location = 'hall'
        elif '4' in choice:
            location = 'r door'
        elif '5' in choice:
            location = 'r vent'
        elif '6' in choice:
            location = 'parts'
            
    elif location == 'l door':
        print('You are at the left door\n\n1 - Flash Door\n2 - ', end='')
        if leftDoorDown:
            print('Open Door\n3 - Leave')
        else:
            print('Close Door\n3 - Leave')
        choice = input('\n> ')
        
        if '1' in choice:
            cls()
            if status['bonnie'] == 1:
                input('bonnie was there')
            else:
                input('there was nobody there')
                
        elif '2' in choice:
            leftDoorDown = 1 - leftDoorDown
        
        elif '3' in choice:
            location = 'center'

    elif location == 'r door':
        print('You are at the right door\n\n1 - Flash Door\n2 - ', end='')
        if rightDoorDown:
            print('Open Door\n3 - Leave')
        else:
            print('Close Door\n3 - Leave')
            
        choice = input('\n> ')
        
        if '1' in choice:
            cls()
            if status['chica'] == 1:
                input('chica was there')
            else:
                input('there was nobody there')
                
        elif '2' in choice:
            rightDoorDown = 1 - rightDoorDown
        
        elif '3' in choice:
            location = 'center'
    
    elif location == 'hall':
        print('You are in the hallway\n\n1 - Flash Hallway\n2 - Leave')
        choice = input('\n> ')
        
        if '1' in choice:
            cls()
            if status['w foxy'] == 1:
                input('withered foxy was there')
                foxyFlashed = 1
            elif status['t chica'] == 1:
                input('toy chica was there')
            elif status['t freddy'] == 1:
                input('toy freddy was there')
            elif status['mangle'] == 1:
                input('mangle was there')
            elif status['w bonnie'] == 1:
                input('withered bonnie was there')
            elif status['w freddy'] == 1:
                input('withered freddy was there')
            else:
                input('there was nobody there')
    
        if '2' in choice:
            location = 'center'
    
    elif location == 'l vent':
        print('You are at the left vent\n\n1 - Flash Vent\n2 - Leave')
        choice = input('\n> ')
        
        if '1' in choice:
            cls()
            if status['t chica'] == 2:
                input('toy chica was there')
            elif status['bb'] == 1:
                input('bb was there')
            else:
                input('there was nobody there')
    
        if '2' in choice:
            location = 'center'
    
    elif location == 'r vent':
        print('You are at the right vent\n\n1 - Flash Vent\n2 - Leave')
        choice = input('\n> ')
        
        if '1' in choice:
            cls()
            if status['t bonnie'] == 1:
                input('toy bonnie was there')
            elif status['mangle'] == 2:
                input('mangle was there')
            else:
                input('there was nobody there')
    
        if '2' in choice:
            location = 'center'
    
    elif location == 'parts':
        print('You are in Parts and Service\n\n1 - View Pirate\'s Cove\n2 - Check Music Box\n3 - Leave')
        choice = input('\n> ')
        
        if '1' in choice:
            cls()
            if status['foxy'] == 0:
                input('the curtains are closed')
            elif status['foxy'] == 1:
                input('foxy is peeking out the curtains')
            elif status['foxy'] == 2:
                input('foxy is leaning out the curtains')
            elif status['foxy'] == 3:
                input('foxy is gone')

        if '2' in choice:
            pass
    
        if '3' in choice:
            location = 'center'
    

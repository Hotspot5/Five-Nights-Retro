import threading
import time
import random
import constants

def cls():
    print("\033[H\033[2J\033[3J", end="")

def death(animatronic):
    global dead
    dead = 1
    cls()
    input(f'you got killed by {animatronic}')
    

MOVEMENT_FREQ = constants.MOVEMENT_FREQ
NIGHT_LEN = constants.NIGHT_LEN
ANIMATRONIC_GAP = constants.ANIMATRONIC_GAP
PUPPET_MAX_TIMER = constants.PUPPET_MAX_TIMER
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
puppetTimer = 0
dead = False

leftDoorDown = False
rightDoorDown = False
maskOn = False
foxyFlashed = False
batteryStolen = False

hallBusy = False
leftVentBusy = False
rightVentBusy = False
officeBusy = False

def gameloop():
    global nightTimer, status, hallBusy, officeBusy, leftVentBusy, rightVentBusy, foxyFlashed, batteryStolen
      
    start = time.time()
    
    while nightTimer < NIGHT_LEN:
        
        waitTime = MOVEMENT_FREQ - (time.time() - start)
        time.sleep(waitTime)
        nightTimer += waitTime
            
        start = time.time()
        
        for animatronic in status:
            
            
            
            ########## ANIMATRONIC CODE: SCRIPTED EVENTS
            
            
            
            if animatronic == 'freddy' and status[animatronic] == 1 and rightDoorDown:
                status[animatronic] = 0
                continue
                
            if animatronic == 'bonnie' and status[animatronic] == 1 and leftDoorDown:
                status[animatronic] = 0
                continue
                
            if animatronic == 'chica' and status[animatronic] == 1 and rightDoorDown:
                status[animatronic] = 0
                continue
                
            if animatronic == 'foxy' and status[animatronic] == 3:
                if leftDoorDown:
                    status[animatronic] = 0
                    continue
                else:
                    death('Foxy')
                    return
                
            if animatronic in ['t freddy', 'w freddy', 'w bonnie'] and status[animatronic] == 2:
                if not maskOn:
                    if animatronic == 't freddy':
                        death('Toy Freddy')
                    elif animatronic == 'w freddy':
                        death('Withered Freddy')
                    else:
                        death('Withered Bonnie')
                    return
                else:
                    status[animatronic] = 0
                    officeBusy = False
                    continue
                
            if animatronic == 't bonnie' and status[animatronic] == 1 and maskOn:
                status[animatronic] = 0
                rightVentBusy = False
                continue
            
            if animatronic == 'mangle' and status[animatronic] == 2 and maskOn:
                status[animatronic] = 0
                rightVentBusy = False
                continue
                
            if animatronic == 't chica' and status[animatronic] == 2 and maskOn:
                status[animatronic] = 0
                leftVentBusy = False
                continue
                
            if animatronic == 'bb' and status[animatronic] == 1 and maskOn:
                status[animatronic] = 0
                leftVentBusy = False
                continue
            
            if animatronic == 'w chica' and status[animatronic] == 1:
                if not maskOn:
                    death('Withered Chica')
                    return
                else:
                    status[animatronic] = 0
                    officeBusy = False
                    continue
            
            if animatronic == 'w foxy' and status[animatronic] == 1:
                if foxyFlashed:
                    status[animatronic] = 0
                    foxyFlashed = False
                    continue
                
                
            
            ########## END ##########
            
            
                
            if random.random() < AI_LEVELS[animatronic] / 20:
                status[animatronic] += 1
                 
                 
                 
                 ########## ANIMATRONIC CODE: POTENTIAL EVENTS ##########
                 
                 
                 
                if animatronic == 'freddy':
                    if status[animatronic] == 2:
                            death('Freddy Fazbear')
                            return
            
                if animatronic == 'bonnie':
                    if status[animatronic] == 2:
                            death('Bonnie')
                            return
                
                if animatronic == 'chica':
                    if status[animatronic] == 2:
                            death('Chica')
                            return
                
                if animatronic in ['t freddy', 'w freddy', 'w bonnie']:
                    if status[animatronic] == 1:
                        if hallBusy:
                            status[animatronic] = 0
                        else:
                            hallBusy = True
                    if status[animatronic] == 2:
                        if not officeBusy:
                            hallBusy = False
                            officeBusy = True
                        else:
                            status[animatronic] = 1
                
                if animatronic == 't bonnie':
                    if status[animatronic] == 1:
                        if rightVentBusy:
                            status[animatronic] = 0
                        else:
                            rightVentBusy = True
                    if status[animatronic] == 2:
                        death('Toy Bonnie')
                        return
                
                if animatronic == 'mangle':
                    if status[animatronic] == 1:
                        if hallBusy:
                            status[animatronic] = 0
                        else:
                            hallBusy = True
                    if status[animatronic] == 2:
                        if rightVentBusy:
                            status[animatronic] = 1
                        else:
                            rightVentBusy = True
                            hallBusy = False
                    if status[animatronic] == 3:
                        death('Mangle')
                        return
                
                if animatronic == 't chica':
                    if status[animatronic] == 1:
                        if hallBusy:
                            status[animatronic] = 0
                        else:
                            hallBusy = True
                    if status[animatronic] == 2:
                        if leftVentBusy:
                            status[animatronic] = 1
                        else:
                            leftVentBusy = True
                            hallBusy = False
                    if status[animatronic] == 3:
                        death('Toy Chica')
                        return
                
                if animatronic == 'bb':
                    if status[animatronic] == 1:
                        if leftVentBusy:
                            status[animatronic] = 0
                        else:
                            leftVentBusy = True
                    if status[animatronic] == 2:
                        batteryStolen = True
                        status[animatronic] = 3
                
                if animatronic == 'w chica':
                    if not officeBusy:
                        officeBusy = True
                    else:
                        status[animatronic] = 0
                
                if animatronic == 'w foxy':
                    if status[animatronic] == 2:
                        death('Withered Foxy')
                        return
                    
                
                
                ########## END ##########
                
                
                
            time.sleep(ANIMATRONIC_GAP)
        
threading.Thread(target=gameloop).start()

location = 'center'

while not dead:
    
    cls()
    
    if location == 'center':
        
        if officeBusy:
            
            if status['t freddy'] == 2:
                print('BLACKOUT SEQUENCE: Toy Freddy') 
            elif status['w freddy'] == 2:
                print('BLACKOUT SEQUENCE: Withered Freddy')
            elif status['w bonnie'] == 2:
                print('BLACKOUT SEQUENCE: Withered Bonnie')
            else:
                print('BLACKOUT SEQUENCE: Withered Chica')
                
            print('\nA - Put On Mask')
            choice = input('\n> ')
            if 'a' in choice.lower():
                location = 'mask'
                maskOn = True
        else:
            print('Where do you want to go?\n\n1 - Left Door\n2 - Left Vent\n3 - Hallway\n4 - Right Door\n5 - Right Vent\n6 - Parts and Service\n\nA - Put on Mask')
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
            elif 'a' in choice.lower():
                location = 'mask'
                maskOn = True
    
    elif location == 'mask':
        print('A - Take Off Mask')
        choice = input('\n> ')
        if 'a' in choice.lower():
            maskOn = False
            location = 'center'
            
    elif location == 'l door':
        print('You are at the left door\n\n1 - Flash Door\n2 - ', end='')
        if leftDoorDown:
            print('Open Door\n3 - Leave')
        else:
            print('Close Door\n3 - Leave')
        choice = input('\n> ')
        
        if '1' in choice and not batteryStolen:
            cls()
            if status['bonnie'] == 1:
                input('bonnie was there')
            else:
                input('there was nobody there')
                
        elif '2' in choice:
            leftDoorDown = bool(1 - leftDoorDown)
        
        elif '3' in choice:
            location = 'center'

    elif location == 'r door':
        print('You are at the right door\n\n1 - Flash Door\n2 - ', end='')
        if rightDoorDown:
            print('Open Door\n3 - Leave')
        else:
            print('Close Door\n3 - Leave')
            
        choice = input('\n> ')
        
        if '1' in choice and not batteryStolen:
            cls()
            if status['chica'] == 1:
                input('chica was there')
            else:
                input('there was nobody there')
                
        elif '2' in choice:
            rightDoorDown = bool(1 - rightDoorDown)
        
        elif '3' in choice:
            location = 'center'
    
    elif location == 'hall':
        print('You are in the hallway\n\n1 - Flash Hallway\n2 - Leave')
        choice = input('\n> ')
        
        if '1' in choice and not batteryStolen:
            if status['w foxy'] == 1:
                foxyFlashed = True
            cls()
            if status['t chica'] == 1:
                input('toy chica was there')
            elif status['t freddy'] == 1:
                input('toy freddy was there')
            elif status['mangle'] == 1:
                input('mangle was there')
            elif status['w bonnie'] == 1:
                input('withered bonnie was there')
            elif status['w freddy'] == 1:
                input('withered freddy was there')
            elif status['w foxy'] == 1:
                input('withered foxy was there')
            else:
                input('there was nobody there')
    
        if '2' in choice:
            location = 'center'
    
    elif location == 'l vent':
        print('You are at the left vent\n\n1 - Flash Vent\n2 - Leave')
        choice = input('\n> ')
        
        if '1' in choice and not batteryStolen:
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
        
        if '1' in choice and not batteryStolen:
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
    

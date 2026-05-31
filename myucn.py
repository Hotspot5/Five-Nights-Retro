import threading
import time
import random
import constants

def cls():
    print("\033[H\033[2J\033[3J", end="")

def death(animatronic):
    global dead
    dead = True
    cls()
    print('YOU DIED\n')
    if animatronic == 'freddy':
        print(constants.FREDDY)
    elif animatronic == 'bonnie':
        print(constants.BONNIE)
    elif animatronic == 'chica':
        print(constants.CHICA)
    elif animatronic == 'foxy':
        print(constants.FOXY)
    elif animatronic == 't freddy':
        print(constants.T_FREDDY_IN_OFFICE)
    elif animatronic == 't bonnie':
        print(constants.T_BONNIE)
    elif animatronic == 't chica':
        print(constants.T_CHICA_IN_HALL)
    elif animatronic == 'w freddy':
        print(constants.W_FREDDY_IN_OFFICE)
    elif animatronic == 'w bonnie':
        print(constants.W_BONNIE)
    elif animatronic == 'w chica':
        print(constants.W_CHICA)
    elif animatronic == 'w foxy':
        print(constants.W_FOXY)
    elif animatronic == 'mangle':
        print(constants.MANGLE_IN_OFFICE)
    elif animatronic == 'springtrap':
        print(constants.SPRINGTRAP_NEAR)
    elif animatronic == 'puppet':
        print(constants.PUPPET)
    else:
        print(constants.ITSME)
    while True:
        input()
    

NIGHT_LEN = constants.NIGHT_LEN
PUPPET_UNWIND_TIME = constants.PUPPET_UNWIND_TIME
AI_LEVELS = constants.AI_LEVELS
SLOW_MOVE = constants.SLOW_MOVE
EASY_ANIMATRONICS = constants.EASY_ANIMATRONICS

movementFreq = 4

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
puppetWound = 1
doorTimer = 0
lastLureTime = 0

dead = False
leftDoorDown = False
rightDoorDown = False
maskOn = False
foxyFlashed = False
batteryStolen = False
puppetWinding = False

hallBusy = False
leftVentBusy = False
rightVentBusy = False
officeBusy = False

movedLast = []
moving = []

def timers():
    global movementFreq, nightTimer, puppetWound, doorTimer
    while not dead and nightTimer < NIGHT_LEN:
        time.sleep(1/10)
        
        nightTimer += 0.1
        
        if not puppetWinding:
            puppetWound -= 0.1/PUPPET_UNWIND_TIME
            if puppetWound <= 0:
                death('puppet')
                return
        else:
            puppetWound += 0.01
            if puppetWound > 1:
                puppetWound = 1
            
        if leftDoorDown or rightDoorDown:
            doorTimer += 0.1
        elif doorTimer > 0:
            doorTimer -= 0.1
            
        movementFreq = 4 - doorTimer / 5

def gameloop():
    
    global nightTimer, status, hallBusy, officeBusy, leftVentBusy, rightVentBusy, foxyFlashed, batteryStolen, moving, movedLast
    
    while nightTimer < NIGHT_LEN and not dead:
        
        for animatronic in status:
            
            
            
            ########## ANIMATRONIC CODE: SCRIPTED EVENTS ##########
            
            
            
            if animatronic == 'freddy' and status[animatronic] == 1 and rightDoorDown:
                status[animatronic] = 0
                moving.append(animatronic)
                continue
                
            if animatronic == 'bonnie' and status[animatronic] == 1 and leftDoorDown:
                status[animatronic] = 0
                moving.append(animatronic)
                continue
                
            if animatronic == 'chica' and status[animatronic] == 1 and rightDoorDown:
                status[animatronic] = 0#
                moving.append(animatronic)
                continue
                
            if animatronic == 'foxy' and status[animatronic] == 3:
                if leftDoorDown:
                    status[animatronic] = 0
                    continue
                else:
                    death('foxy')
                    return
                
            if animatronic in ['t freddy', 'w freddy', 'w bonnie'] and status[animatronic] == 2:
                if not maskOn:
                    if animatronic == 't freddy':
                        death('t freddy')
                    elif animatronic == 'w freddy':
                        death('w freddy')
                    else:
                        death('w bonnie')
                    return
                else:
                    status[animatronic] = 0
                    officeBusy = False
                    moving.append(animatronic)
                    continue
                
            if animatronic == 't bonnie' and status[animatronic] == 1 and maskOn:
                status[animatronic] = 0
                rightVentBusy = False
                moving.append(animatronic)
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
                moving.append(animatronic)
                continue
            
            if animatronic == 'w chica' and status[animatronic] == 1:
                if not maskOn:
                    death('w chica')
                    return
                else:
                    status[animatronic] = 0
                    officeBusy = False
                    moving.append(animatronic)
                    continue
            
            if animatronic == 'w foxy' and status[animatronic] == 1:
                if foxyFlashed:
                    status[animatronic] = 0
                    foxyFlashed = False
                    moving.append(animatronic)
                    continue

            if animatronic == 'itsme' and status[animatronic] == 1:
                if maskOn:
                    status[animatronic] = 0
                    continue
                else:
                    death('itsme')
                    return
                
            div = 20
            if animatronic in EASY_ANIMATRONICS or animatronic in SLOW_MOVE:
                div = 30
            if animatronic == 'w chica' or animatronic == 'itsme':
                div = 80
                
            if random.random() < AI_LEVELS[animatronic] / div:
                status[animatronic] += 1
                
                if animatronic in SLOW_MOVE:
                    if animatronic in movedLast:
                        status[animatronic] -= 1
                    else:
                        moving.append(animatronic)
                 
                 
                 
                 ########## ANIMATRONIC CODE: RANDOM EVENTS ##########
                 
                 
                 
                if animatronic == 'freddy':
                    if status[animatronic] == 2:
                            death('freddy')
                            return
            
                elif animatronic == 'bonnie':
                    if status[animatronic] == 2:
                            death('bonnie')
                            return
                
                elif animatronic == 'chica':
                    if status[animatronic] == 2:
                            death('chica')
                            return
                
                elif animatronic in ['t freddy', 'w freddy', 'w bonnie']:
                    if status[animatronic] == 1:
                        if hallBusy:
                            status[animatronic] = 0
                            moving.remove(animatronic)
                        else:
                            hallBusy = True
                    elif status[animatronic] == 2:
                        if not officeBusy:
                            hallBusy = False
                            officeBusy = True
                        else:
                            status[animatronic] = 1
                            moving.remove(animatronic)
                
                elif animatronic == 't bonnie':
                    if status[animatronic] == 1:
                        if rightVentBusy:
                            status[animatronic] = 0
                            moving.remove(animatronic)
                        else:
                            rightVentBusy = True
                    elif status[animatronic] == 2:
                        death('t bonnie')
                        return
                
                elif animatronic == 'mangle':
                    if status[animatronic] == 1:
                        if hallBusy:
                            status[animatronic] = 0
                        else:
                            hallBusy = True
                    elif status[animatronic] == 2:
                        if rightVentBusy:
                            status[animatronic] = 1
                        else:
                            rightVentBusy = True
                            hallBusy = False
                    elif status[animatronic] == 3:
                        rightVentBusy = False
                    elif status[animatronic] == 4:
                        death('mangle')
                        return
                                   
                elif animatronic == 't chica':
                    if status[animatronic] == 1:
                        if hallBusy:
                            status[animatronic] = 0
                        else:
                            hallBusy = True
                    elif status[animatronic] == 2:
                        if leftVentBusy:
                            status[animatronic] = 1
                        else:
                            leftVentBusy = True
                            hallBusy = False
                    elif status[animatronic] == 3:
                        death('t chica')
                        return
                
                elif animatronic == 'bb':
                    if status[animatronic] == 1:
                        if leftVentBusy:
                            status[animatronic] = 0
                            moving.remove(animatronic)
                        else:
                            leftVentBusy = True
                    elif status[animatronic] == 2:
                        batteryStolen = True
                
                elif animatronic == 'w chica':
                    if not officeBusy:
                        officeBusy = True
                    else:
                        status[animatronic] = 0
                        moving.remove(animatronic)
                
                elif animatronic == 'w foxy':
                    if status[animatronic] == 2:
                        death('w foxy')
                        return

                elif animatronic == 'springtrap':
                    if status['springtrap'] == 4:
                        death('springtrap')
                        return
                    
            time.sleep(movementFreq / 14)
            
        movedLast = moving.copy()
        moving = []
        
threading.Thread(target=gameloop).start()
threading.Thread(target=timers).start()

location = 'center'



########## USER INTERFACE AND ACTIONS ##########



while not dead and nightTimer < NIGHT_LEN:
    
    cls()
    
    if status['itsme'] == 1:
        print('itsme\n')
        
    if nightTimer / NIGHT_LEN > 1/6:
        print(f'{int(nightTimer / NIGHT_LEN*6)} A.M.\n')
    else:
        print('12 A.M.\n')
        
    if puppetWound < 0.2:
        print('WARNING: MUSIC BOX VERY LOW\n')
    elif puppetWound < 0.4:
        print('WARNING: music box low\n')
    
    if location == 'center':
        
        if officeBusy:
            
            if status['t freddy'] == 2:
                print(constants.T_FREDDY_IN_OFFICE) 
            elif status['w freddy'] == 2:
                print(constants.W_FREDDY_IN_OFFICE)
            elif status['w bonnie'] == 2:
                print(constants.W_BONNIE)
            else:
                print(constants.W_CHICA)
                
            print(f'\n{'='*40}\n\n[A] - Put On Mask\n\n{'='*40}')
            choice = input('\n> ')
            if 'a' in choice.lower():
                location = 'mask'
                maskOn = True
            
        else:
            
            if status['bb'] > 1:
                print('BB HAS STOLEN YOUR BATTERIES\n')
            if status['mangle'] == 3:
                print('MANGLE IS ON THE ROOF\n')
                
            print('You are in the center of the room.')
            print()
            print('='*40)
            print()
            print('Where do you want to go?')
            print()
            print('='*40)
            print()
            print(f'[1] - Left Door\n[2] - Right Door\n\n[3] - Left Vent\n[4] - Right Vent\n\n[5] - Parts & Service\n\n[6] - Hallway\n\n{'='*40}\n\n[A] - Put On Mask')
            #print('Where do you want to go?\n\n1 - Left Door\n2 - Left Vent\n3 - Hallway\n4 - Right Door\n5 - Right Vent\n6 - Parts and Service\n\nA - Put on Mask')
            choice = input('\n> ')
            if '1' in choice:
                location = 'l door'
            elif '2' in choice:
                location = 'r door'
            elif '3' in choice:
                location = 'l vent'
            elif '4' in choice:
                location = 'r vent'
            elif '5' in choice:
                location = 'parts'
            elif '6' in choice:
                location = 'hall'
            elif 'a' in choice.lower():
                location = 'mask'
                maskOn = True
    
    elif location == 'mask':
        print(constants.MASK)
        input('[enter] - Take Off the Mask')
        maskOn = False
        location = 'center'
            
    elif location == 'l door':
        print('You are at the Left Door.')
        print()
        print('='*40)
        print()
        print('What do you want to do?')
        print()
        print('='*40)
        print()
        print('[1] - Flash the door\n\n[2] - ', end='')
        if leftDoorDown:
            print(f'Open Door\n\n{'='*40}\n\n[3] - Leave')
        else:
            print(f'Close Door\n\n{'='*40}\n\n[3] - Leave')
        choice = input('\n> ')
        
        if '1' in choice and not batteryStolen:
            cls()
            if status['bonnie'] == 1:
                input(constants.BONNIE)
            else:
                input(constants.DOOR)
                
        elif '2' in choice:
            leftDoorDown = bool(1 - leftDoorDown)
        
        elif '3' in choice:
            location = 'center'

    elif location == 'r door':
        print('You are at the Right Door.')
        print()
        print('='*40)
        print()
        print('What do you want to do?')
        print()
        print('='*40)
        print()
        print('[1] - Flash the door\n\n[2] - ', end='')
        if rightDoorDown:
            print(f'Open the Door\n\n{'='*40}\n\n[3] - Leave')
        else:
            print(f'Close the Door\n\n{'='*40}\n\n[3] - Leave')
            
        choice = input('\n> ')
        
        if '1' in choice and not batteryStolen:
            cls()
            if status['chica'] == 1:
                input(constants.CHICA)
            else:
                input(constants.DOOR)
                
        elif '2' in choice:
            rightDoorDown = bool(1 - rightDoorDown)
        
        elif '3' in choice:
            location = 'center'
    
    elif location == 'hall':
        print('You are in the Hallway.')
        print()
        print('='*40)
        print()
        print('What do you want to do?')
        print()
        print('='*40)
        print()
        print(f'[1] - Flash the Hallway\n\n{'='*40}\n\n[2] - Leave the Hallway')
        choice = input('\n> ')
        
        if '1' in choice and not batteryStolen:
            if status['w foxy'] == 1:
                foxyFlashed = True
            cls()
            if status['t chica'] == 1:
                input(constants.T_CHICA_IN_HALL)
            elif status['t freddy'] == 1:
                input(constants.T_FREDDY_IN_HALL)
            elif status['mangle'] == 1:
                input(constants.MANGLE_IN_HALL)
            elif status['w bonnie'] == 1:
                input(constants.W_BONNIE)
            elif status['w freddy'] == 1:
                input(constants.W_FREDDY_IN_HALL)
            elif status['w foxy'] == 1:
                input(constants.W_FOXY)
            else:
                input(constants.FLASHLIGHT)
    
        elif '2' in choice:
            location = 'center'
    
    elif location == 'l vent':
        print('You are beside the Left Vent.')
        print()
        print('='*40)
        print()
        print('What do you want to do?')
        print()
        print('='*40)
        print()
        print(f'[1] - Flash the Vent\n\n{'='*40}\n\n[2] - Leave')
        choice = input('\n> ')
        
        if '1' in choice and not batteryStolen:
            cls()
            if status['t chica'] == 2:
                input(constants.T_CHICA_IN_VENT)
            elif status['bb'] == 1:
                input(constants.BB_IN_VENT)
            else:
                input(constants.EMPTY_VENT)
    
        elif '2' in choice:
            location = 'center'
    
    elif location == 'r vent':
        print('You are beside the Right Vent.')
        print()
        print('='*40)
        print()
        print('What do you want to do?')
        print()
        print('='*40)
        print()
        print(f'[1] - Flash the Vent\n\n{'='*40}\n\n[2] - Leave')
        choice = input('\n> ')
        
        if '1' in choice and not batteryStolen:
            cls()
            if status['t bonnie'] == 1:
                input(constants.T_BONNIE_IN_VENT)
            elif status['mangle'] == 2:
                input(constants.MANGLE_IN_VENT)
            else:
                input(constants.EMPTY_VENT)
    
        elif '2' in choice:
            location = 'center'
    
    elif location == 'parts':
        print('You are in Parts & Service.')
        print()
        print('='*40)
        print()
        print('What do you want to do?')
        print()
        print('='*40)
        print()
        print(f'[1] - View Pirate\'s Cove\n\n[2] - Visit the Prize Corner\n\n[3] - Look in the Back Room\n\n{'='*40}\n\n[4] - Leave')
        choice = input('\n> ')
        
        if '1' in choice:
            cls()
            if status['foxy'] == 0:
                input(constants.CURTAIN_CLOSED)
            elif status['foxy'] == 1:
                input(constants.CURTAIN_1)
            elif status['foxy'] == 2:
                input(constants.CURTAIN_2)
            elif status['foxy'] == 3:
                input(constants.CURTAIN_OPEN)

        elif '2' in choice:
            location = 'prize'
        
        elif '3' in choice:
            location = 'back'
    
        elif '4' in choice:
            location = 'center'
    
    elif location == 'prize':
        print('You are in the Prize Corner.')
        print()
        print('='*40)
        print()
        print('What do you want to do?')
        print()
        print('='*40)
        print()
        print(f'[1] - Check Music Bok\n\n[2] - Wind Up Music Box\n\n{'='*40}\n\n[3] - Leave')
        choice = input('\n> ')
        
        if '1' in choice:
            cls()
            print('='*40)
            print()
            print(f'Music Box Level: {round(puppetWound*100)}%')
            print()
            print('='*40)
            input('\n> ')
        
        elif '2' in choice:
            cls()
            puppetWinding = True
            print('='*40)
            print()
            print(f'Winding Music Box...')
            print()
            print('='*40)
            print()
            print('[enter] - Stop Winding the Music Box')
            input('\n> ')
            puppetWinding = False
        
        elif '3' in choice:
            location = 'parts'

    elif location == 'back':
        print('You are in the Back Room.')
        print()
        print('='*40)
        print()
        print('What do you want to do?')
        print()
        print('='*40)
        print()
        print(f'[1] - Flash the Room\n\n[2] - Use Audio Lure\n\n{'='*40}\n\n[3] - Leave')
        choice = input('\n> ')
        
        if '1' in choice:
            cls()
            if status['springtrap'] == 0:
                input(constants.PARTS_AND_SERVICE)
            if status['springtrap'] == 1:
                input(constants.SPRINGTRAP_VERY_FAR)
            if status['springtrap'] == 2:
                input(constants.SPRINGTRAP_FAR)
            if status['springtrap'] == 3:
                input(constants.SPRINGTRAP_NEAR)
                
        elif '2' in choice:
            if time.time() - lastLureTime > 7:
                lastLureTime = time.time()
                if status['springtrap'] > 0:
                    status['springtrap'] -= 1
            else:
                cls()
                input(f'{'='*40}\n\nThe Audio Lure did not work.\n\n{'='*40}\n\n> ')
        
        elif '3' in choice:
            location = 'parts'

if not dead:
    cls()
    print('you won!')
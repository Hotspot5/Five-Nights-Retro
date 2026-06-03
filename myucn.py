import threading
import time
import random
import constants
from pygame import mixer

def cls():
    print("\033[H\033[2J\033[3J", end="")

def death(animatronic):
    global dead
    if nightTimer < NIGHT_LEN:
        dead = True
        cls()
        print('YOU DIED\n')
        mixer.pause()
        if animatronic == 'freddy':
            sounds['fnaf1jumpscare'].play()
            print(constants.FREDDY)
        elif animatronic == 'bonnie':
            sounds['fnaf1jumpscare'].play()
            print(constants.BONNIE)
        elif animatronic == 'chica':
            sounds['fnaf1jumpscare'].play()
            print(constants.CHICA)
        elif animatronic == 'foxy':
            sounds['fnaf1jumpscare'].play()
            print(constants.FOXY)
        elif animatronic == 't freddy':
            sounds['fnaf2jumpscare'].play()
            print(constants.T_FREDDY_IN_OFFICE)
        elif animatronic == 't bonnie':
            sounds['fnaf2jumpscare'].play()
            print(constants.T_BONNIE)
        elif animatronic == 't chica':
            sounds['fnaf2jumpscare'].play()
            print(constants.T_CHICA_IN_HALL)
        elif animatronic == 'w freddy':
            sounds['fnaf2jumpscare'].play()
            print(constants.W_FREDDY_IN_OFFICE)
        elif animatronic == 'w bonnie':
            sounds['fnaf2jumpscare'].play()
            print(constants.W_BONNIE)
        elif animatronic == 'w chica':
            sounds['fnaf2jumpscare'].play()
            print(constants.W_CHICA)
        elif animatronic == 'w foxy':
            sounds['fnaf2jumpscare'].play()
            print(constants.W_FOXY)
        elif animatronic == 'mangle':
            sounds['fnaf2jumpscare'].play()
            print(constants.MANGLE_IN_OFFICE)
        elif animatronic == 'springtrap':
            sounds['fnaf3jumpscare'].play()
            print(constants.SPRINGTRAP_NEAR)
        elif animatronic == 'puppet':
            sounds['fnaf2jumpscare'].play()
            print(constants.PUPPET)
        else:
            sounds['itsmejumpscare'].play()
            print(constants.ITSME)
        while True:
            input()

def checkWarning():
    if (status['freddy'] > 2
        or status['bonnie'] > 2
        or status['chica'] > 2
        or status['foxy'] > 2
        or status['t freddy'] > 2
        or status['t bonnie'] > 2
        or status['t chica'] > 2
        or status['w freddy'] > 2
        or status['w bonnie'] > 2
        or status['w chica'] > 2
        or status['w foxy'] == 1
        or status['mangle'] > 2
        or status['springtrap'] > 2
        or puppetWound < 0.125
        or status['itsme'] == 1
        or status['bb'] > 2
        ):
        return True
    return False

mixer.pre_init(
    frequency=44100,
    size=-16,
    channels=2,
    buffer=512
)

mixer.init()
mixer.set_num_channels(128)

sounds = {
    'bblaugh': mixer.Sound('sounds\\bblaugh.wav'), 
    'bbhello': mixer.Sound('sounds\\bbhello.wav'), 
    'fnaf2ambience': mixer.Sound('sounds\\fnaf2ambience.ogg'), 
    'fnaf2jumpscare': mixer.Sound('sounds\\fnaf2jumpscare.wav'), 
    'fnaf2walk': mixer.Sound('sounds\\fnaf2walk.wav'), 
    'fnaf3jumpscare': mixer.Sound('sounds\\fnaf3jumpscare.wav'), 
    'manglenoise': mixer.Sound('sounds\\manglenoise.wav'), 
    'manglewalk': mixer.Sound('sounds\\manglewalk.wav'), 
    'maskbreath': mixer.Sound('sounds\\maskbreath.wav'), 
    'maskoff': mixer.Sound('sounds\\maskoff.wav'), 
    'maskon': mixer.Sound('sounds\\maskon.wav'), 
    'musicbox': mixer.Sound('sounds\\musicbox.wav'), 
    'puppetout': mixer.Sound('sounds\\puppetout.wav'), 
    'siren': mixer.Sound('sounds\\siren.wav'), 
    'startday': mixer.Sound('sounds\\startday.wav'), 
    'ventwalk': mixer.Sound('sounds\\ventwalk.wav'), 
    'wind': mixer.Sound('sounds\\wind.wav'), 
    'doorbang': mixer.Sound('sounds\\bang.wav'), 
    'kitchen': mixer.Sound('sounds\\chicakitchen.wav'), 
    'circus': mixer.Sound('sounds\\circus.wav'), 
    'doorclose': mixer.Sound('sounds\\doorclose.wav'),
    'error': mixer.Sound('sounds\\error.wav'), 
    'fan': mixer.Sound('sounds\\fan.wav'), 
    'fnaf1ambience': mixer.Sound('sounds\\fnaf1ambience.ogg'), 
    'fnaf1jumpscare': mixer.Sound('sounds\\fnaf1jumpscare.wav'), 
    'foxyrun': mixer.Sound('sounds\\foxyrun.wav'), 
    'itsmejumpscare': mixer.Sound('sounds\\itsmejumpscare.wav'), 
    'robotvoice': mixer.Sound('sounds\\robotvoice.wav'), 
    'fnaf1walk': mixer.Sound('sounds\\fnaf1walk.wav'), 
    'win': mixer.Sound('sounds\\win.wav'), 
    'windowscare': mixer.Sound('sounds\\windowscare.wav'), 
    'freddylaugh': mixer.Sound('sounds\\freddylaugh.wav'), 
    'fnaf3walk': mixer.Sound('sounds\\fnaf3walk.wav'), 
    'blackout': mixer.Sound('sounds\\blackout.wav'), 
    'itsmelaugh': mixer.Sound('sounds\\itsmelaugh.wav'), 
    'flashlight': mixer.Sound('sounds\\flashlight.wav'), 
    'run': mixer.Sound('sounds\\run.wav'), 
    'piratesong': mixer.Sound('sounds\\piratesong.wav')
}
    

NIGHT_LEN = constants.NIGHT_LEN
PUPPET_UNWIND_TIME = constants.PUPPET_UNWIND_TIME
AI_LEVELS = constants.AI_LEVELS

MOVES_3 = constants.MOVES_3
MOVES_2 = constants.MOVES_2
MOVES_1 = constants.MOVES_1

movementFreq = 5

status = {
    'freddy': 0, 
    'bonnie': 0, 
    'chica': 0, 
    'foxy': 0, 
    'itsme': 0, 
    't freddy': 0, 
    't bonnie': 0, 
    't chica': 0, 
    'mangle': 0, 
    'w freddy': 0, 
    'w bonnie': 0, 
    'w chica': 0, 
    'w foxy': 0, 
    'bb': 0, 
    'springtrap': 0, 
    #puppet is here
}

Timers = {
    'freddy': 0, 
    'bonnie': 0, 
    'chica': 0, 
    'foxy': 0, 
    't bonnie': 0, 
    't chica': 0, 
    'bb': 0, 
    'springtrap': 0, 
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

playingMusicBox = False
playingWarning = False

hallBusy = False
leftVentBusy = False
rightVentBusy = False
officeBusy = False

def timers():
    global movementFreq, nightTimer, puppetWound, doorTimer, playingWarning, Timers, status, batteryStolen
    lastTime = time.time()
    while not dead and nightTimer < NIGHT_LEN:
        
        time.sleep(1/10)
        
        nightTimer += time.time()-lastTime
        lastTime = time.time()
        
        for animatronic in Timers:
            
            if animatronic in ('freddy', 'chica'):
        
                if status[animatronic] >= 3:
                    Timers[animatronic] += 0.1
                    if Timers[animatronic] > movementFreq * 20 / AI_LEVELS[animatronic]:
                        if not rightDoorDown:
                            death(animatronic)
                        else:
                            Timers[animatronic] = 0
                            status[animatronic] = 0
                            if animatronic == 'freddy':
                                sounds['freddylaugh'].play()
                            else:
                                sounds['fnaf1walk'].play()
            
            elif animatronic in ('foxy', 'bonnie'):
                
            
                if status[animatronic] >= 3:
                    Timers[animatronic] += 0.1
                    if Timers[animatronic] > movementFreq * 20 / AI_LEVELS[animatronic]:
                        if not leftDoorDown:
                            death(animatronic)
                        else:
                            Timers[animatronic] = 0
                            status[animatronic] = 0
                            if animatronic == 'bonnie':
                                sounds['fnaf1walk'].play()
                            else:
                                sounds['doorbang'].play()
            
            elif animatronic in ('t bonnie', 't chica', 'bb'):
                
                if status[animatronic] >= 3:
                    Timers[animatronic] += 0.1
                    if Timers[animatronic] > movementFreq * 20 / AI_LEVELS[animatronic]:
                        if not maskOn and animatronic != 'bb':
                            death(animatronic)
                        elif not maskOn and animatronic == 'bb':
                            batteryStolen = True
                            leftVentBusy = False
                            sounds['bblaugh'].play(loops=-1)
                        else:
                            Timers[animatronic] = 0
                            status[animatronic] = 0
                            if animatronic in ('t bonnie', 'bb'):
                                sounds['ventwalk'].play()
            
            elif animatronic == 'w foxy':
                
                if status[animatronic] >= 1:
                    Timers[animatronic] += 0.1
                    if Timers[animatronic] > movementFreq * 20 / AI_LEVELS[animatronic]:
                        if not foxyFlashed:
                            death(animatronic)
                        else:
                            Timers[animatronic] = 0
                            status[animatronic] = 0
            
            elif animatronic == 'springtrap':
            
                if status[animatronic] >= 3:
                    Timers[animatronic] += 0.1
                    if Timers[animatronic] > movementFreq * 20 / AI_LEVELS[animatronic]:
                        death(animatronic)

        
        if not puppetWinding:
            puppetWound -= 0.1/PUPPET_UNWIND_TIME
            if puppetWound <= 0:
                sounds['puppetout'].play()
                time.sleep(3.5)
                death('puppet')
                return
        else:
            puppetWound += 0.025
            if puppetWound > 1:
                puppetWound = 1
        
        warning = checkWarning()
        if warning and not playingWarning:
            sounds['siren'].play(loops=-1)
            playingWarning = True
        elif not warning and playingWarning:
            sounds['siren'].stop()
            playingWarning = False
            
        if leftDoorDown or rightDoorDown:
            doorTimer += 0.1
        elif doorTimer > 0:
            doorTimer -= 0.05
        
        if doorTimer >= 12:
            death('foxy')

def gameloop():
    
    global nightTimer, status, hallBusy, officeBusy, leftVentBusy, rightVentBusy, foxyFlashed, batteryStolen, location, puppetWinding, foxyTimer
    
    while nightTimer < NIGHT_LEN and not dead:
        
        for animatronic in status:
            
            
            
            ########## ANIMATRONIC CODE: SCRIPTED EVENTS ##########
            
            
            
            if animatronic == 'freddy' and status[animatronic] == 3 and rightDoorDown:
                status[animatronic] = 0
                sounds['freddylaugh'].play()
                continue
                
            elif animatronic == 'bonnie' and status[animatronic] == 3 and leftDoorDown:
                status[animatronic] = 0
                sounds['fnaf1walk'].play()
                continue
                
            elif animatronic == 'chica' and status[animatronic] == 3 and rightDoorDown:
                status[animatronic] = 0
                sounds['fnaf1walk'].play()
                continue
                
            elif animatronic == 'foxy' and status[animatronic] >= 3 and leftDoorDown:
                foxyTimer = 0
                status['foxy'] = 0
                sounds['doorbang'].play()
                
            elif animatronic in ['t freddy', 'w freddy', 'w bonnie'] and status[animatronic] == 3:
                if not maskOn:
                    if animatronic == 't freddy':
                        death('t freddy')
                    elif animatronic == 'w freddy':
                        death('w freddy')
                    else:
                        death('w bonnie')
                    return
                else:
                    sounds['blackout'].stop()
                    status[animatronic] = 0
                    officeBusy = False
                    continue
                
            elif animatronic == 't bonnie' and status[animatronic] == 3 and maskOn:
                status[animatronic] = 0
                rightVentBusy = False
                sounds['ventwalk'].play()
                continue
            
            elif animatronic == 'mangle' and status[animatronic] == 3 and maskOn:
                status[animatronic] = 0
                rightVentBusy = False
                sounds['ventwalk'].play()
                sounds['manglenoise'].stop()
                continue
                
            elif animatronic == 't chica' and status[animatronic] == 3 and maskOn:
                status[animatronic] = 0
                leftVentBusy = False
                continue
                
            elif animatronic == 'bb' and status[animatronic] == 3 and maskOn:
                status[animatronic] = 0
                leftVentBusy = False
                sounds['ventwalk'].play()
                continue
            
            elif animatronic == 'w chica' and status[animatronic] == 3:
                if not maskOn:
                    death('w chica')
                    return
                else:
                    sounds['blackout'].stop()
                    status[animatronic] = 0
                    officeBusy = False
                    continue
            
            elif animatronic == 'w foxy' and status[animatronic] == 1:
                if foxyFlashed:
                    status[animatronic] = 0
                    foxyFlashed = False
                    continue

            elif animatronic == 'itsme' and status[animatronic] == 1:
                if maskOn:
                    status[animatronic] = 0
                    sounds['itsmelaugh'].play()
                    continue
                else:
                    death('itsme')
                    return
             
            div = 20
            #if animatronic in MOVES_3:
            #    div = 30
            if animatronic in MOVES_2:
                div = 40
            #elif animatronic in MOVES_1:
            #    div = 80
            
            #input(AI_LEVELS[animatronic] / div)
            if random.random() < AI_LEVELS[animatronic] / div:
                status[animatronic] += 1                 
                 
                 
                 
                 ########## ANIMATRONIC CODE: RANDOM EVENTS ##########
                 
                 
                 
                if animatronic == 'freddy':
                    if status[animatronic] == 3:
                        sounds['freddylaugh'].play()
                        sounds['robotvoice'].play()
                    elif status[animatronic] < 4:
                        sounds['freddylaugh'].play()                 
            
                elif animatronic == 'bonnie':
                    if status[animatronic] < 4:
                        sounds['fnaf1walk'].play()
                                     
                elif animatronic == 'chica':
                    if status[animatronic] == 1:
                        sounds['fnaf1walk'].play()
                        sounds['kitchen'].play(loops=-1)
                    elif status[animatronic] == 2:
                        sounds['fnaf1walk'].play()
                        sounds['kitchen'].stop()
                    elif status[animatronic] == 3:
                        sounds['fnaf1walk'].play()
         
                elif animatronic == 'foxy':
                    pass #sounds['piratesong'].play()
           
                elif animatronic in ['t freddy', 'w freddy', 'w bonnie']:
                    if status[animatronic] == 2:
                        if hallBusy:
                            status[animatronic] = 0
                        else:
                            hallBusy = True
                            sounds['fnaf2walk'].play()
                    elif status[animatronic] == 3:
                        if not officeBusy:
                            hallBusy = False
                            officeBusy = True
                            sounds['blackout'].play()
                            location = 'center'
                            puppetWinding = False
                            sounds['musicbox'].stop()
                            sounds['wind'].stop()
                        else:
                            status[animatronic] = 1
                    else:
                        sounds['fnaf2walk'].play()
                                     
                elif animatronic == 't bonnie':
                    if status[animatronic] == 3:
                        if rightVentBusy:
                            status[animatronic] = 0        
                        else:
                            rightVentBusy = True
                            sounds['ventwalk'].play()
                    elif status[animatronic] == 1:
                        sounds['fnaf2walk'].play()
                    elif status[animatronic] == 2:
                        sounds['ventwalk'].play()
                
                elif animatronic == 'mangle':
                    if status[animatronic] == 1:
                        if hallBusy:
                            status[animatronic] = 0
                        else:
                            hallBusy = True
                            sounds['manglewalk'].play()
                    elif status[animatronic] == 2:
                        hallBusy = False
                        sounds['ventwalk'].play()
                    elif status[animatronic] == 3:
                        if rightVentBusy:
                            status[animatronic] = 1
                        else:
                            rightVentBusy = True
                            hallBusy = False
                            sounds['ventwalk'].play()
                            sounds['manglenoise'].play(loops=-1)
                    elif status[animatronic] == 4:
                        rightVentBusy = False
                        sounds['ventwalk'].play()
                    elif status[animatronic] == 5:
                        death('mangle')
                        return
                                   
                elif animatronic == 't chica':
                    if status[animatronic] == 1:
                        if hallBusy:
                            status[animatronic] = 0
                        else:
                            hallBusy = True
                            sounds['fnaf2walk'].play()
                    elif status[animatronic] == 2:
                        hallBusy = False
                        sounds['ventwalk'].play()
                    elif status[animatronic] == 3:
                        if leftVentBusy:
                            status[animatronic] = 1
                        else:
                            leftVentBusy = True
                            hallBusy = False
                            sounds['ventwalk'].play()
                
                elif animatronic == 'bb':
                    if status[animatronic] == 3:
                        if leftVentBusy:
                            status[animatronic] = 0
                        else:
                            leftVentBusy = True
                            sounds['bbhello'].play()
                    elif status[animatronic] == 1:
                        sounds['bbhello'].play()
                    elif status[animatronic] == 2:
                        sounds['ventwalk'].play()
                
                elif animatronic == 'w chica':
                    if status[animatronic] == 3:
                        if not officeBusy:
                            officeBusy = True
                            sounds['blackout'].play()
                            location = 'center'
                            puppetWinding = False
                            sounds['musicbox'].stop()
                            sounds['wind'].stop()
                        else:
                            status[animatronic] = 0
                    else:
                        sounds['fnaf2walk'].play()
                
                elif animatronic == 'w foxy':
                    pass

                elif animatronic == 'springtrap':
                    sounds['fnaf3walk'].play()
                    
                elif animatronic == 'itsme':
                    sounds['itsmelaugh'].play()
                    if not maskOn:
                        cls()
                        print(constants.ITSME)
            
           # print(nightTimer)
            time.sleep(movementFreq / len(status))
        
threading.Thread(target=gameloop).start()
threading.Thread(target=timers).start()

location = 'center'

sounds['fnaf1ambience'].play(loops=-1)
sounds['fnaf2ambience'].play(loops=-1)

sounds['fan'].set_volume(0.2)
sounds['piratesong'].set_volume(0.5)
sounds['kitchen'].set_volume(0.25)

sounds['fan'].play(loops=-1)



########## USER INTERFACE AND ACTIONS ##########



while not dead and nightTimer < NIGHT_LEN:
    
    cls()
    
    print(nightTimer)
        
    if nightTimer / NIGHT_LEN > 1/6:
        print(f'{int(nightTimer / NIGHT_LEN*6)} A.M.\n')
    else:
        print('12 A.M.\n')
        
    if puppetWound < 0.125 or doorTimer > 9:
        print('⚠ ⚠ ⚠\n')
    elif puppetWound < 0.25 or doorTimer > 6:
        print('⚠\n')
        
    
    if location == 'center':
        
        if officeBusy:
            
            if status['t freddy'] == 3:
                print(constants.T_FREDDY_IN_OFFICE) 
            elif status['w freddy'] == 3:
                print(constants.W_FREDDY_IN_OFFICE)
            elif status['w bonnie'] == 3:
                print(constants.W_BONNIE)
            else:
                print(constants.W_CHICA)
                
            print(f'\n{'='*40}\n\n[A] - Put On Mask\n\n{'='*40}')
            choice = input('\n> ')
            if 'a' in choice.lower():
                location = 'mask'
                maskOn = True
                sounds['maskon'].play()
            
        else:
            
            print()
            print('You are in the office.')
            print()
            print('='*40)
            print()
            print('Where do you want to go?')
            print()
            print('='*40)
            print()
            print(f'[1] - Left Door\n[2] - Right Door\n\n[3] - Left Vent\n[4] - Right Vent\n\n[5] - Hallway\n\n[6] - Parts & Service\n\n[7] - Pirate Cove\n\n{'='*40}\n\n[A] - Put On Mask')
            #print('Where do you want to go?\n\n1 - Left Door\n2 - Left Vent\n3 - Hallway\n4 - Right Door\n5 - Right Vent\n6 - Parts and Service\n\nA - Put on Mask')
            choice = input('\n> ')
            
            if '1' in choice:
                location = 'l door'
                sounds['run'].play()
                
            elif '2' in choice:
                location = 'r door'
                sounds['run'].play()
                
            elif '3' in choice:
                
                if not batteryStolen:
                    sounds['flashlight'].play()
                    cls()
                    if status['t chica'] == 3:
                        input(constants.T_CHICA_IN_VENT)
                    elif status['bb'] == 3:
                        input(constants.BB_IN_VENT)
                    else:
                        input(constants.EMPTY_VENT)
                else:
                    sounds['error'].play()
                    
            elif '4' in choice:
                
                if not batteryStolen:
                    sounds['flashlight'].play()
                    cls()
                    if status['t bonnie'] == 3:
                        input(constants.T_BONNIE_IN_VENT)
                    elif status['mangle'] == 3:
                        input(constants.MANGLE_IN_VENT)
                    else:
                        input(constants.EMPTY_VENT)
                    
                else:
                    sounds['error'].play()
                
            elif '5' in choice:
                
                if not batteryStolen:
                    sounds['flashlight'].play()
                    if status['w foxy'] == 1:
                        foxyFlashed = True
                    cls()
                    if status['t chica'] == 1:
                        input(constants.T_CHICA_IN_HALL)
                    elif status['t freddy'] == 2:
                        input(constants.T_FREDDY_IN_HALL)
                    elif status['mangle'] == 1:
                        input(constants.MANGLE_IN_HALL)
                    elif status['w bonnie'] == 2:
                        input(constants.W_BONNIE)
                    elif status['w freddy'] == 2:
                        input(constants.W_FREDDY_IN_HALL)
                    elif status['w foxy'] == 1:
                        input(constants.W_FOXY)
                    else:
                        input(constants.FLASHLIGHT)
                else:
                    sounds['error'].play()
                
            elif '6' in choice:
                location = 'parts'
                sounds['run'].play()
            
            elif '7' in choice:
                sounds['flashlight'].play()
                cls()
                if status['foxy'] == 0:
                    input(constants.CURTAIN_CLOSED)
                elif status['foxy'] == 1:
                    input(constants.CURTAIN_1)
                elif status['foxy'] == 2:
                    input(constants.CURTAIN_2)
                elif status['foxy'] == 3:
                    input(constants.CURTAIN_OPEN)
                
            elif 'a' in choice.lower():
                location = 'mask'
                maskOn = True
    
    elif location == 'mask':
        print(constants.MASK)
        sounds['maskon'].play()
        sounds['maskbreath'].play(loops=-1)
        input('> ')
        maskOn = False
        location = 'center'
        sounds['maskbreath'].stop()
        sounds['maskoff'].play()
            
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
            print(f'Open the Door\n\n{'='*40}\n\n[3] - Leave')
        else:
            print(f'Close the Door\n\n{'='*40}\n\n[3] - Leave')
        choice = input('\n> ')
        
        if '1' in choice and not batteryStolen:
            cls()
            sounds['flashlight'].play()
            if status['bonnie'] == 3:
                sounds['windowscare'].play()
                input(constants.BONNIE)
                
            else:
                input(constants.DOOR)
        elif '1' in choice and batteryStolen:
            sounds['error'].play()
                
        elif '2' in choice:
            leftDoorDown = bool(1 - leftDoorDown)
            sounds['doorclose'].play()
        
        elif '3' in choice:
            location = 'center'
            sounds['run'].play()

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
            sounds['flashlight'].play()
            if status['chica'] == 3:
                sounds['windowscare'].play()
                input(constants.CHICA)
            else:
                input(constants.DOOR)
        elif '1' in choice and batteryStolen:
            sounds['error'].play()
                
        elif '2' in choice:
            rightDoorDown = bool(1 - rightDoorDown)
            sounds['doorclose'].play()
        
        elif '3' in choice:
            location = 'center'
            sounds['run'].play()
    
    elif location == 'parts':
        print('You are in Parts & Service.')
        print()
        print('='*40)
        print()
        print('What do you want to do?')
        print()
        print('='*40)
        print()
        print(f'[1] - Visit the Prize Corner\n\n[2] - Look in the Back Room\n\n{'='*40}\n\n[3] - Leave')
        choice = input('\n> ')

        if '1' in choice:
            
            cls()
            
            if not playingMusicBox:
                sounds['musicbox'].play(loops=-1)
                playingMusicBox = True
        
            print('='*40)
            print()
            print(f'Music Box Level: {round(puppetWound*100)}%')
            print()
            print('='*40)
            input('\n> ')
            print()
            
            sounds['wind'].play(loops=-1)
            puppetWinding = True
            print('='*40)
            print()
            print(f'Winding Music Box...')
            print()
            print('='*40)
            print()
            input('\n> ')
            puppetWinding = False
            sounds['wind'].stop()
        
            sounds['musicbox'].stop()
            sounds['run'].play()
            playingMusicBox = False
        
        elif '2' in choice:
            location = 'back'
            sounds['run'].play()
    
        elif '3' in choice:
            location = 'center'
            sounds['run'].play()

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
        
        if '1' in choice and not batteryStolen:
            sounds['flashlight'].play()
            cls()
            if status['springtrap'] == 0:
                input(constants.PARTS_AND_SERVICE)
            if status['springtrap'] == 1:
                input(constants.SPRINGTRAP_VERY_FAR)
            if status['springtrap'] == 2:
                input(constants.SPRINGTRAP_FAR)
            if status['springtrap'] == 3:
                input(constants.SPRINGTRAP_NEAR)
        elif '1' in choice and batteryStolen:
            sounds['error'].play()
                
        elif '2' in choice:
            if time.time() - lastLureTime > 9:
                lastLureTime = time.time()
                sounds['bbhello'].play()
                if status['springtrap'] > 0:
                    status['springtrap'] -= 1
            else:
                cls()
                sounds['error'].play()
                input(f'{'='*40}\n\nThe Audio Lure did not work.\n\n{'='*40}\n\n> ')
        
        elif '3' in choice:
            location = 'parts'
            sounds['run'].play()

if not dead:
    cls()
    mixer.pause()
    sounds['win'].play()
    print('''                                                                                                                                          
                                                                                                                                          
YYYYYYY       YYYYYYY                                     WWWWWWWW                           WWWWWWWW                                 !!! 
Y:::::Y       Y:::::Y                                     W::::::W                           W::::::W                                !!:!!
Y:::::Y       Y:::::Y                                     W::::::W                           W::::::W                                !:::!
Y::::::Y     Y::::::Y                                     W::::::W                           W::::::W                                !:::!
YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu        W:::::W           WWWWW           W:::::W ooooooooooo   nnnn  nnnnnnnn    !:::!
   Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u         W:::::W         W:::::W         W:::::Woo:::::::::::oo n:::nn::::::::nn  !:::!
    Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u          W:::::W       W:::::::W       W:::::Wo:::::::::::::::on::::::::::::::nn !:::!
     Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u           W:::::W     W:::::::::W     W:::::W o:::::ooooo:::::onn:::::::::::::::n!:::!
      Y:::::::Y   o::::o     o::::ou::::u    u::::u            W:::::W   W:::::W:::::W   W:::::W  o::::o     o::::o  n:::::nnnn:::::n!:::!
       Y:::::Y    o::::o     o::::ou::::u    u::::u             W:::::W W:::::W W:::::W W:::::W   o::::o     o::::o  n::::n    n::::n!:::!
       Y:::::Y    o::::o     o::::ou::::u    u::::u              W:::::W:::::W   W:::::W:::::W    o::::o     o::::o  n::::n    n::::n!!:!!
       Y:::::Y    o::::o     o::::ou:::::uuuu:::::u               W:::::::::W     W:::::::::W     o::::o     o::::o  n::::n    n::::n !!! 
       Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu              W:::::::W       W:::::::W      o:::::ooooo:::::o  n::::n    n::::n     
    YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u               W:::::W         W:::::W       o:::::::::::::::o  n::::n    n::::n !!! 
    Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u                W:::W           W:::W         oo:::::::::::oo   n::::n    n::::n!!:!!
    YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu                 WWW             WWW            ooooooooooo     nnnnnn    nnnnnn !!! 
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          ''')
    while True:
        input()
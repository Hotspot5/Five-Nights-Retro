import threading
import time
import random
import constants

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
    't foxy': 0, 
    'w freddy': 0, 
    'w bonnie': 0, 
    'w chica': 0, 
    'w foxy': 0, 
    'bb': 0, 
    'mangle': 0, 
    'puppet': 0, 
    'springtrap': 0, 
    'itsme': 0, 
}

nightTimer = 0

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
                 print(animatronic, status[animatronic])
            time.sleep(ANIMATRONIC_GAP)
    return
        
gameloop()
print('done')
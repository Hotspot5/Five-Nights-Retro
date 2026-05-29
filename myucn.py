import threading
import time
import random

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

AIlevels = {
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

movementFreq = 5
nightLength = 360
animatronicGap = 0.25

movementTimer = 0
nightTimer = 0

fps = 60

def gameloop(fps):
    start = time.time()
    
    while nightTimer < nightLength:
        
        while time.time() - start < movementFreq:
            time.sleep(1/fps)
            
        start = time.time()
        nightTimer += movementFreq
        
        for animatronic in status:
            if random.random() < AIlevels[animatronic] / 20:
                 status[animatronic] += 1
             time.sleep(animatronicGap)
    return
        
            
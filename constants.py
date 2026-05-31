AI_LEVELS = {
    'freddy': 3, 
    'bonnie': 3, 
    'chica': 3, 
    'foxy': 3, 
    't freddy': 3, 
    't bonnie': 3, 
    't chica': 3,  
    'w freddy': 3, 
    'w bonnie': 3, 
    'w chica': 3, 
    'w foxy': 3, 
    'bb': 3, 
    'mangle': 3, 
    'puppet': 3, 
    'springtrap': 3, 
    'itsme': 3, 
}

SLOW_MOVE = ['freddy', 'bonnie', 'chica', 't freddy', 't bonnie', 'w freddy', 'w bonnie', 'w foxy', 'bb', 'w chica']
EASY_ANIMATRONICS = ['foxy', 't chica']

NIGHT_LEN = 321

if AI_LEVELS['puppet']:
    PUPPET_UNWIND_TIME = NIGHT_LEN / AI_LEVELS['puppet'] - 1
else:
    PUPPET_UNWIND_TIME = NIGHT_LEN*200


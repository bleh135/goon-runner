room1 = (
    20,
    "yello, welcome to dun dun duuun...your the goon runner.................DUN DUN DUUUUUUUUUUUN",
    ["poop_in_quots"],
    [["N", 12, False],
     ["W", 19, False],
     ["S", 28, False],
     ["E", 21, False]
        ])

room2 = (
    12,
    "yello, welcome to dun dun duuun.........you first enemy..........DUN DUN DUUUUUUUUUUUN",
    ["slipper_with_1_use...", "small_silly_cute_bug..."],
    [["N", 4, False],
     ["E", 13, False],
     ["S", 20, False]
        
        ])



room3 = (
    4,
    "yello, welcome to dun dun duuun.........te plase wid armor..........DUN DUN DUUUUUUUUUUUN",
    ["sword_with_1_use...", "small_silly_cute_armor..."],
    [["S", 12, False],
     
        ])


room4 = (
    28,
    "yello, welcome to dun dun duuun.........te locke room..........DUN DUN DUUUUUUUUUUUN",
    ["key_with_1_use...", "small_silly_cute_air..."],
    [["N", 20, False],
     ["E", 29, False]]
        
        )


room5 = (
    21,
    "yello, welcome to dun dun duuun.........lokd dor...........DUN DUN DUUUUUUUUUUUN",
    ["lokd dor..."],
    [["W", 20, False],
     ["S", 29, False],
     ["E", 22, True]
      ])


room6 = (
    22,
    "yello, welcome to dun dun duuun.........bos...........DUN DUN DUUUUUUUUUUUN",
    ["air..........woosh.....", "bos..."],
    [["E", 22, False] 
  
         ])

rooms = {
    20: room1,
    12: room2,
    4: room3,
    28: room4,
    21: room5,
    22: room6,
    }

def show_room(room):
    
    (number, greeting, odjects, doors)=room
    print(greeting)
    print("----------------------------------------")
    # list the inventory
    print ('you -> HAVE  :O <-  ___item___')
    for item in inventory:
        print ('* ' + item)
    print()
    # list objects in the room
    print ("you see___item___")
    for item in odjects:
        print ('* ' + item)
        print()        
    print()

    print('you see___exit___')
    for door in doors:
        (direction, dest, locked) = door
        print('* ' +  direction)
    print()

def go (direction):
    """
    moves from the current room
    paramiters*****************
    **********
    direction (string): the direction to move n e w s
    
    updat crrent room if valid
    """
    global current_room
    global rooms
    doors = current_room[3]
    
    for door in doors:
        (door_direction, destination, locked) = door
        if door_direction.lower() == direction.lower():
            if locked:
                print('L O C K E D...')
                print()
                return
            else:
                current_room = rooms[destination]
                return
    print ('ayo, says gullible on the cealing          stupid cant go thru wallsgon')
    

def take (thing):
    """
    Takes an object - remove from room +to inventory
    Paramiters:
    ***********
    thing (str): the object to take)
    """
    global current_room
    global inventory
    
    objects = current_room[2]
    if (thing in objects):
        objects.remove(thing)
        inventory.append(thing)
        if thing.lower() == "bos...":
            print("the massive ogre strolls twards you scarily'\nboom boom boom!he stomps on you dangerouslyand breaks your...'/nneck then turns you into a pankake this is the bad ending of our story")
            exit()
    else:
        print('yo, its no- hmm it doesnt - EXIST    BEEPING STOP idiot lolli ssess')
        
def sword():
    '''
    kills enemy
    '''
    global current_room
    # is there an enemy in the room I am in in?
    # If yes, remove it
    # If no, jeer at player
    objects = current_room[2] # this gets the objects for the current room
    if current_room[0] == 12:
        #objects.remove('small_silly_cute_bug')
        print('"You slash at the bug, but your sword bounces off!')
    
    if current_room[0] == 22:
        objects.remove ('bos...')
        print("VICTORY you have slain the ogre the happy ending")
        print(" \o/    ")
        print("  [")
        print("  A")
        exit()
        
    else:
        print ('you swing around the sword like a maniac')
    
        
def unlock():
    '''
    unlocks all doors
    '''
    global current_room
    doors = current_room[3] # list of all the doors in this room
    for door in doors:
        door[2]=False
        
def use (thing):
    """
uses the specific thing in the current room
paramiters
----------
thing (str) the thing to use
"""
    global inventory
    global current_room
    
    # todo  chek ting is in inventory
    if thing in inventory:
        if thing== 'poop_in_quots':
            print('hhmmppphhhrrrraaaattt')
        elif thing== 'slipper_with_1_use...':
            print('slap!')
        elif thing== 'small_silly_cute_bug...':
            print('OUCH!!!')
        elif thing== 'small_silly_cute_armor...':
            print('chink')
        elif thing== 'small_silly_cute_air...':
            print('wooooosh')
        elif thing== 'sword_with_1_use...':
            sword()
        elif thing== 'key_with_1_use...':
            unlock()
        elif thing== 'lokd_dor...':
            print('BANG,BANG,BOOSH!!!!')
        elif thing== 'air..........woosh.....':
            print('woooooooooooooooooooooooosh')
        elif thing== 'bos...':
            sword()
        else:
            print("Don't know how to use that...")
    else:
        print ('hehehe U NOT HAVE THAT THING IDIOT')
        # insult them...
    #todo ian if for each
        
        # coontnude
        
        
current_room = rooms[20]


inventory = []

while True:

    show_room(current_room)
    cmd = input('enter command: >')
    bits = cmd.split(' ')
    action = bits[0]
    qualifier = bits[1]
    print('action: ' + action)
    print('qualifier: ' + qualifier)

    action = action.lower()
    if action == 'go':
        go(qualifier)
    elif action == 'take':
        take(qualifier)
    elif action == 'use':
       use(qualifier)
    else:
        print('cOmMaNd NoT fOuNd.  NO COMMAND CHEATS LAST TIME, S T O P!                idiot stupid *BEEP*')
        print('*********************************************************')
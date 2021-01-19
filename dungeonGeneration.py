import random
import os

os.system('cls')
# randomize overall dungeon rooms
overall_dungeon_room = random.randint(5, 10)


def gen_room_events(rooms):

    # Generate room events
    while(rooms >= 0 ):
        

    num_doors = random.randint(0, 3)
    num_traps = random.randint(0, 5)


print("There are " + str(overall_dungeon_room) + " rooms in this dungeon")


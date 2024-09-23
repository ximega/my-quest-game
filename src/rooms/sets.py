from src.rooms.tier1 import *

room_init.set_next_rooms([
    (room1, 'west')
])

room1.set_next_rooms([
    (room_init, 'east'),
    (room2, 'north')
])

room2.set_next_rooms([
    (room1, 'south')
])
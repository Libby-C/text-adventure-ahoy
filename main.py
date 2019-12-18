from room import Room
from item import Item

# Set up the kitchen
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

# set up the dining room
dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

# set up the dining hall
ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

# link the rooms togeter
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# create an Item
goblet = Item("goblet", 10)
goblet.set_description("A shiny, ornate goblet with jewel encrusted around the rim.")

# create a loop to allow the player move between rooms
# input needs to be raw_input() to work in python2
# current_room = kitchen
# while True:
#     print("\n")
#     current_room.get_details()
#     command = input("> ")
#     current_room = current_room.move(command)

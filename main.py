import rpg

# Set up the kitchen
kitchen = rpg.Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

# set up the dining room
dining_hall = rpg.Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

# set up the dining hall
ballroom = rpg.Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

# link the rooms togeter
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# create Items
goblet = rpg.Item("goblet", 10)
goblet.set_description("A shiny, ornate goblet with jewel encrusted around the rim.")

cheese = rpg.Item("cheese", 1)
cheese.set_description("A hunk of strong and delicious cheese.")

crowbar = rpg.Item("crowbar", 2)
crowbar.set_description("A crowbar. Good for prying and smashing.")

# Create a character
libby = rpg.Enemy("Libby", "A smol Christmas elf vampire hybrid with plans for world domination")
libby.describe()

# set the conversation for libby character and make it talk
# libby.set_conversation("Hello, I'm here to tell you about Mass Effect. Garrus for LYFE!")
# libby.talk()
# # set set_weakness
# libby.set_weakness("onion")
# # fight the enemy
# print("What will you fight with?")
# weapon = input("> ")
# libby.fight(weapon)

# create Dave the zombie
dave = rpg.Enemy("Dave", "A lonely zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)
dave.set_item(crowbar)

# put the goblet in the Ballroom
ballroom.set_item(goblet)
kitchen.set_item(cheese)

# create a loop to allow the player move between rooms
# input needs to be raw_input() to work in python2
current_room = kitchen
backpack = []

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if inhabitant is not None:
        inhabitant.describe()
    if item is not None:
        item.describe()
    command = input("> ")
    command_words = command.split()
    # Check whether a direction was typed
    print(command_words)
    if "move" in command_words:
        for word in command_words:
            if word in ["north", "south", "east", "west"]:
                current_room = current_room.move(word)
    elif command == "talk":
        inhabitant.talk()
    elif "fight" in command_words:
        if inhabitant == None or isinstance(inhabitant, Friend):
            print("There is no one here to fight with")
        else:
            print("What will you fight " + inhabitant.name + " with?")
            weapon = input("> ")
            # need to check if weapon matches any item.name for all objects in the backpack
            weapons = ", ".join(item.name for item in backpack)
            if weapon in weapons:
                if inhabitant.fight(weapon) == True:
                    # What happens if you win?
                    print("You live to fight another day!")
                    current_room.set_character(None)
                else:
                    # What happens if you lose?
                    print("Oh dear, you've been defeated.")
                    print("That's it, you're dead.")
                    dead = True
            else:
                print("You don't have a " + weapon + " in your bag.")
    elif "take" in command_words:
        # take the item, put it in your backpack and remove it from the room
        print("You take the %s and put it in your backpack." % item.name )
        backpack.append(item)
        current_room.set_item(None)
    elif "backpack" in command_words:
        items = ", ".join(item.name for item in backpack)
        # check to see if there is anything in the bag
        if len(items) != 0:
            print("In your backpack you currently have: " + items)
        else:
            print("You don't have anything in your back")
    # add option to steal from characters in the current room, (fight them first?)

    # set class variable somewhere so that the player wins after defeating a certain amoutn of enemies?

class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print(self.name + " linked rooms: " + repr(self.linked_rooms))

    def get_details(self):
        print("-------------")
        print("The %s" % self.name)
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The %s is %s" % (room.name, direction))

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("\nYou can't go that way")
            return self

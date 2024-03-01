class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, description):
        self.description = description

    def link_room(self, room, direction):
        self.linked_rooms[direction] = room

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print(f"The {room.name} is {direction}")

    def move(self, direction):
        return self.linked_rooms.get(direction, None)

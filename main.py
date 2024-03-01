from room import Room
from character import Enemy, Friend
from item import Item


kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

library = Room("Library")
library.set_description("Rows of ancient books line the walls, dust floating in the air.")

garden = Room("Garden")
garden.set_description("A lush garden full of blooming flowers and a small pond.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(library, "east")
library.link_room(dining_hall, "west")
kitchen.link_room(garden, "west")
garden.link_room(kitchen, "east")

dave = Enemy("Dave", "A smelly zombie", "cheese")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
kitchen.character = dave

cheese = Item("Cheese", "A large and smelly block of cheese")
dining_hall.item = cheese

def show_instructions():
    print("\nRPG Game Instructions:")
    print("----------------------")
    print("Commands:")
    print("  [direction]           - Move to the room in the specified direction (north, south, east, west)")
    print("  talk                  - Talk to the character in the room to find out if the enemy is there")
    print("  fight                 - Engage in combat with the enemy in the room")
    print("  take                  - Pick up the item in the room")
    print("  [Iteam collected]     - Show your items")
    print("  quit                  - End the game")
    print("\nExample: To move north, type 'north'. To talk, type 'talk'.")
    print("---------------------------------------------------------------\n")



def main():
    current_room = kitchen
    backpack = []
    show_instructions()

    while True:
        print("\nYou are currently in the", current_room.name)
        current_room.get_details()
        command = input("> ").lower()

        if command in ["north", "south", "east", "west"]:
            next_room = current_room.move(command)
            show_instructions()
            if next_room:
                current_room = next_room
                show_instructions()
            else:
                print("You can't go that way!")
        elif command == "talk":
            if current_room.character:
                current_room.character.talk()
            else:
                print("There's no one here to talk to.")
        elif command == "fight":
            if isinstance(current_room.character, Enemy):
                show_instructions()
                fight_with = input("What will you fight with? ")
                if fight_with in backpack:
                    if current_room.character.fight(fight_with):
                        print("You won the fight!")
                        current_room.character = None
                        print("Congratulations! You have completed the game!")
                        break
                else:
                    print("You lost the fight.")
                    print("Game Over!")
                    break
            else:
                print("There's no one here to fight.")
        elif command == "take":
            if current_room.item:
                backpack.append(current_room.item.name)
                show_instructions()
                print(f"*************** --> You put the {current_room.item.name} in your backpack.<-- ************")
                current_room.item = None
            else:
                print("There's nothing here to take.")
        elif command == "inventory":
            show_instructions()
            print("You have:")
            for item in backpack:
                print(item)
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("I don't understand that command.")
            show_instructions()

if __name__ == "__main__":
    main()
class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk.")

class Enemy(Character):
    def __init__(self, name, description, weakness):
        super().__init__(name, description)
        self.weakness = weakness.lower() 

    def fight(self, item):
        if item.lower() == self.weakness.lower():
            print(f"You fend off {self.name} with the {item}.")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

class Friend(Character):
    def __init__(self, name, description):
        super().__init__(name, description)

    def hug(self):
        print(f"You hug {self.name}. How sweet!")

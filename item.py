# NEEDED FUNCTIONS: Return Name, Return Description
# NEEDED ATTRIBUTES: Name, Description
# SUPERCLASS OF: Equippable, Usable
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getName(self): # Getters and setters for the name variable
        return self.name
    def setName(self, newName):
        self.name = newName

    def getDescription(self): # Getters and setters for the description variable
        return self.description
    def setDescription(self, newDescription):
        self.description = newDescription

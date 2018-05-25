import item
# NEEDED FUNCTIONS: Getters and Setters
# NEEDED ATTRIBUTES: Name, Description, Attack Difference, Intellect Difference
# SUBCLASS OF: item
class Weapon(item.Item):
    
    def __init__(self, name, description, strengthDifference, intellectDifference):
        item.Item.__init__(self, name, description)
        self.strengthDifference = strengthDifference
        self.intellectDifference = intellectDifference

    def getStrengthDifference(self): # Getters and setters for strength
        return self.strengthDifference
    def setStrengthDifference(self, newStrengthDifference):
        self.strengthDifference = newStrengthDifference

    def getIntellectDifference(self): # Getters and setters for  intellect
        return self.intellectDifference
    def setIntellectDifference(self, newIntellectDifference):
        self.intellectDifference = newIntellectDifference

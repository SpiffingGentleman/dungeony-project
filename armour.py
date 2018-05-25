import item
# NEEDED FUNCTIONS: getters and setters
# NEEDED ATTRIBUTES: Name, Description, Attack Difference, Intellect Difference, Defense
# SUBCLASS OF: item
class Armour(item.Item):
    
    def __init__(self, name, description, strengthDifference, intellectDifference, defenseDifference):
        item.Item.__init__(self, name, description)
        self.strengthDifference = strengthDifference
        self.intellectDifference = intellectDifference
        self.defenseDifference = defenseDifference

    def getStrengthDifference(self): # Getters and setters for strength
        return self.strengthDifference
    def setStrengthDifference(self, newStrengthDifference):
        self.strengthDifference = newStrengthDifference

    def getIntellectDifference(self): # Getters and setters for  intellect
        return self.intellectDifference
    def setIntellectDifference(self, newIntellectDifference):
        self.intellectDifference = newIntellectDifference

    def getDefenseDifference(self): # Getters and setters for  defense
        return self.defenseDifference
    def setDefenseDifference(self, newDefenseDifference):
        self.defenseDifference = newDefenseDifference

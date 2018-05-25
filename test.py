import trinket
import weapon
import armour

sord = armour.Armour("sord", "stebs peple", 3, 0, 2)
print(sord.name)
sord.setName("sord ii")
print(sord.name)

if isinstance(sord, weapon.Weapon):
    print("IT WORKS")


print(sord.getDefenseDifference())
sord.setDefenseDifference(5)
print(sord.getDefenseDifference())

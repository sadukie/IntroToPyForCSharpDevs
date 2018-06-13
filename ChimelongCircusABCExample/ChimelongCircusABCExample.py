from ChimelongHorse import ChimelongHorse
from ChimelongMonkey import ChimelongMonkey
from CastMember import CastMember

ch = ChimelongHorse("Horse 1")
ch.move()

cm = ChimelongMonkey()
print("Is the Chimelong Monkey a Cast Member?")
print(isinstance(cm,CastMember))

print("Can the Chimelong Monkey move?")
try:
    cm.move()
except:
    print('ChimelongMonkey is a virtual subclass')

print("=" * 50)
print("Traversing the __class__ chain")
print(cm.__class__)
print(cm.__class__.__class__)
print("Every class is a type.")
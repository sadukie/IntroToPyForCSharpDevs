from Horse import Horse
from CastMember import CastMember

# Multiple inheritance
class ChimelongHorse(Horse, CastMember):
    """Horse from the Chimelong Circus"""
    def __init__(self,name):
        Horse.__init__(name)

    def move(self):
        self.gallop()
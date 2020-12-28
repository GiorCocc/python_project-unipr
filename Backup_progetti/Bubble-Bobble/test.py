from bubble_bobble_basic import Bubble, Dragon, Enemy, Platform, Arena

class DragonCollidePlatform ():
    def __init__(self):
        self._a = Arena((400,400))
        self._p = Platform(self._a, (120,120))
        self._d = Dragon(self._a, (100,100), )

    def testUpCollide(dragon, platform):
        pass
import unittest
from three_in_a_row import Three
import boardgame


class ThreeTest (unittest.TestCase):
    def test_nogray_white(self):
        three = Three(2,2)
        for i in range (4):
            three.play_at(i,i)
        self.assertTrue(three.nogray()==False)

    def test_nogray_black(self):
        three = Three(2,2)
        for i in range (2):
            three.play_at(i,i)
            three.play_at(i,i)
        self.assertTrue(three.nogray()==False)

    def test_half(self):
        three = Three(4,4)
        for i in range (16):
            if i%2==0:
                three.play_at(i,i)
            else:
                three.play_at(i,i)
                three.play_at(i,i)
        self.assertTrue(three.halfcolor()==True)

    def test_contigue(self):
        three = Three(4,4)
        for i in range (3):
            three.play_at(i,i)
        self.assertTrue(three.contigue()==False)
        

if __name__ == '__main__':
    unittest.main()
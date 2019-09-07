import unittest
from MarsRover import MarsRover


class MyTestCase(unittest.TestCase):

    def test_1_area(self):
        a = MarsRover(100, 200, (10, 20), "W")
        self.assertEqual(a.area_length, 100)
        self.assertEqual(a.area_width, 200)

    def test_2_land_point(self):
        a = MarsRover(100, 200, (10, 20), "W")
        self.assertEqual(a.position_x, 10)
        self.assertEqual(a.position_y, 20)

    def test_3_orient(self):
        a = MarsRover(100, 200, (10, 20), "W")
        self.assertEqual(a.oriented, "W")

    def test_4_move1(self):
        a = MarsRover(100, 200, (10, 20), "W")
        self.assertEqual(a.move('f'), (9, 20))
        self.assertEqual(a.move('b'), (10, 20))

        a2 = MarsRover(100, 200, (10, 20), "E")
        self.assertEqual(a2.move('f'), (11, 20))
        self.assertEqual(a2.move('b'), (10, 20))

        a3 = MarsRover(100, 200, (10, 20), "N")
        self.assertEqual(a3.move('f'), (10, 21))
        self.assertEqual(a3.move('b'), (10, 20))

        a4 = MarsRover(100, 200, (10, 20), "S")
        self.assertEqual(a4.move('f'), (10, 19))
        self.assertEqual(a4.move('f'), (10, 18))
        self.assertEqual(a4.move('b'), (10, 19))

    def test_turn(self):
        a = MarsRover(100, 200, (10, 20), "W")
        self.assertEqual(a.turn('l'), "S")
        a = MarsRover(100, 200, (10, 20), "W")
        self.assertEqual(a.turn('r'), "N")

        a = MarsRover(100, 200, (10, 20), "N")
        self.assertEqual(a.turn('l'), "W")
        self.assertEqual(a.turn('l'), "S")
        self.assertEqual(a.turn('r'), "W")

        a = MarsRover(100, 200, (10, 20), "E")
        self.assertEqual(a.turn('l'), "N")
        a = MarsRover(100, 200, (10, 20), "E")
        self.assertEqual(a.turn('r'), "S")
        self.assertEqual(a.turn('r'), "W")

        a = MarsRover(100, 200, (10, 20), "S")
        self.assertEqual(a.turn('r'), "W")
        self.assertEqual(a.turn('l'), "S")

if __name__ == '__main__':
    unittest.main()

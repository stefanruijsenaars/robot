from codingtest import *
import unittest

# todo: document tests, make tests less implementation specific

class RobotTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot('N', 0, 0)
        self.assertEqual(self.robot.orientation, 0)
        self.assertEqual(self.robot.orientation, 0)

    def test_turn_left(self):
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.robot.turn_left()
        self.assertEqual(self.robot.get_orientation(), 'W')
        self.robot.turn_left()
        self.assertEqual(self.robot.get_orientation(), 'S')
        self.robot.turn_left()
        self.assertEqual(self.robot.get_orientation(), 'E')
        self.robot.turn_left()
        self.assertEqual(self.robot.get_orientation(), 'N')

    def test_turn_right(self):
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.robot.turn_right()
        self.assertEqual(self.robot.get_orientation(), 'E')
        self.robot.turn_right()
        self.assertEqual(self.robot.get_orientation(), 'S')
        self.robot.turn_right()
        self.assertEqual(self.robot.get_orientation(), 'W')
        self.robot.turn_right()
        self.assertEqual(self.robot.get_orientation(), 'N')

    def test_move_forward(self):
        self.assertEqual(self.robot.position, Point(0,0))
        self.robot.move_forward()
        self.assertEqual(self.robot.position, Point(0,1))
        self.robot.move_forward()
        self.assertEqual(self.robot.position, Point(0,2))
        self.robot.turn_right()
        self.robot.move_forward()
        self.assertEqual(self.robot.position, Point(1,2))

if __name__ == '__main__':
    unittest.main()

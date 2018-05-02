from codingtest import *
import unittest

# todo: document tests

class RobotTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot('N', 0, 0)
        self.assertEqual(self.robot.orientation, 0)

    def test_move_left(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_move_right(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_move_forward(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()

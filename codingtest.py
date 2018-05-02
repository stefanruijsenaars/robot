# Assumptions:
#
# - We assume it's possible for robots to share a piece of grid.
# - Minimal input validation is OK for purposes of the coding test (we assume valid input).
# - We assume the input is sent as a txt file with all the commands, with the
#   syntax already checked for any issues (big assumption, I know).
# - We ignore newlines in the txt file.
# - Since this is a simple problem, it's OK to chock everything in one big file for now.
# - Once a smelly point, always a smelly point.
# - If a point is smelly, and it's possible for the robot to drop off the world
#   by going in different directions (such as in a corner), we don't allow the
#   robot to drop off in any of those directions (i.e. smells are undirected).
# - Very minimal test coverage is OK given time constraint.

# TODO:
# - input validation
# - further test coverage

# To run the code:
# python codingtest.py < input.txt
#
# (this will output the results to stdout)

import sys
from collections import namedtuple

# Usage: p = Point(x=1, y=2)
Point = namedtuple('Point', ['x','y'])

class Robot:
    """Models a robot with a position and an orientation.

    Attributes:
        orientation (int): direction the robot is facing, where 0 is N, 1 is E, 2 is S, 3 is W
        x (Point): position of the robot

    """

    # Directions, respectively: N E S W.
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))

    # Dictionary that translates input chars into internal representation.
    ORIENTATIONS = {
       'N': 0,
       'E': 1,
       'S': 2,
       'W': 3
    }

    def __init__(self, orientation, x, y):
        """Args:
            orientation (str): direction the robot is facing ('N', 'E', 'S', 'W')
            x (int): x coordinate of the robot
            y (int): y coordinate of the robot
            alive (bool): whether the robot is alive or not
            
        """
        self.orientation = self.ORIENTATIONS[orientation] 
        # this will be None if the robot is dead
        self.position = Point(x=x, y=y) 
        # assumption: new robots are alive
        self.alive = True

    def turn_right(self):
        """Make the robot turn right"""
        pass

    def turn_left(self):
        """Make the robot turn left"""
        pass

    def move_forward(self):
        """Make the robot move forward (note this may lead to robot suicide)"""
        pass

    def die(self):
        """Model a robot death"""
        self.alive = False
        self.position = None

class Grid:
    """Models a grid. For now this is only being used to mark the smelly points and the bounds.
    
    Attributes:
       smelly_points (set of Points): the points where the robot will not be allowed to fall of the map any more.
       x_bound (int): upper right x coordinate
       y_bound (int): upper right y coordinate
    """

    """Grid constructor.

    Args:
        x_bound: upper right x coordinate
        y_bound: upper right y coordinate
    """
    def __init__(self, x_bound, y_bound):
        # assumption: smells are undirected
        self.smelly_points = set([])
        self.x_bound = x_bound
        self.y_bound = y_bound

    """Checks if coordinate is within given bounds.

    Returns:
       True if it is, False otherwise.

    """
    def coordinate_is_within_bounds(x, y):
        pass

    def suicide_allowed_at(x, y):
        """Is the robot allowed to kill theirselves at this coordinate?
        
        Args:
           x (int)
           y (int)

        """
        # If the point is smelly, nope.
        pass

    def mark_point_as_smelly(x, y):
        self.smelly_points.add(Point(x,y))

class Simulation:
    """Simulates robot movements based on instructions.
    
    Attributes:
        robots (list of Robots)
        instructions (list of instructions, where index is same as for robot)
        grid (Grid)
        
    """

    def __init__(self, x_bounds, y_bounds):
        """Simulation constructor
        
        Args:
            x_bounds (int)
            y_bounds (int)
            
        """
        self.robots = []
        self.instructions = []
        self.grid = Grid(x_bounds, y_bounds)

    def run(self):
        """Run a simulation"""
        # for every robot, follow instructions

            # if point is not smelly and move would lead to suicide, kill off robot and mark point as smelly.
            # if point is smelly and move would lead to suicide, do nothing
        pass

def parse_instructions(instructions):
    """Parse the given instructions (separated by newlines)"""
    # if more than 100 chars, throw exception
    # if coordinate larger than 50, throw exception
    pass
    
def main():
    """Runs a simulation based on stdin input and outputs the results to stdout"""

    instructions = []
    for line in sys.stdin:
        instructions.append(line.rstrip("\n"))
    print(instructions)

    # Parse instructions -> output will be a simulation object.
    simulation = parse_instructions(instructions)

    # Run simulation, print results to stdout.
    result = simulation.run()
    for line in result:
        print(line)

if __name__ == "__main__":
    # Will only be executed when this module is run directly.
    main()

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
# - fix inconsistent use of separate x, y as args vs Point

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

    CHAR_ORIENTATIONS = ['N', 'E', 'S', 'W']

    def __init__(self, x, y, orientation):
        """Args:
            orientation (str): direction the robot is facing ('N', 'E', 'S', 'W')
            x (int): x coordinate of the robot
            y (int): y coordinate of the robot
            alive (bool): whether the robot is alive or not
            
        """
        self.orientation = self.ORIENTATIONS[orientation.upper()] 
        # this will be None if the robot is dead
        self.position = Point(x=x, y=y) 
        # assumption: new robots are alive
        self.alive = True

    def turn_right(self):
        """Make the robot turn right"""
        if not self.alive:
            return
        self.orientation = (self.orientation + 1) & 3

    def turn_left(self):
        """Make the robot turn left"""
        if not self.alive:
            return
        self.orientation = (self.orientation - 1) & 3

    def move_forward(self):
        """Make the robot move forward"""
        if not self.alive:
            return
        x = self.position.x + self.SHIFT[self.orientation][0]
        y = self.position.y + self.SHIFT[self.orientation][1]
        self.position = Point(x,y)

    def die(self):
        """Model a robot death"""
        self.alive = False

    def get_orientation(self):
        """Returns a char with the orientation (N, S, W, E)"""
        return self.CHAR_ORIENTATIONS[self.orientation]

class Grid:
    """Models a grid. For now this is only being used to mark the smelly points and the bounds.
    
    Attributes:
       smelly_points (set of Points): the points where the robot will not be allowed to fall of the map any more.
       x_bound (int): upper right x coordinate
       y_bound (int): upper right y coordinate
    """

    def __init__(self, x_bound, y_bound):
        """Grid constructor.

        Args:
            x_bound (int): upper right x coordinate
            y_bound (int): upper right y coordinate
        """
        # assumption: smells are undirected
        self.smelly_points = set([])
        self.x_bound = x_bound
        self.y_bound = y_bound

    def coordinate_is_within_bounds(self, x, y):
        """Checks if coordinate is within given bounds.

        Returns:
            True if it is, False otherwise.

        """
        return x >= 0 and x <= self.x_bound and y >= 0 and y <= self.y_bound

    def suicide_allowed_at(self, x, y):
        """Is the robot allowed to kill theirselves at this coordinate?
        
        Args:
           x (int)
           y (int)

        Returns:
            True if it is, False otherwise.

        """
        # If the point is smelly, do not allow suicide - otherwise, do allow.
        return not Point(x,y) in self.smelly_points

    def mark_point_as_smelly(self, x, y):
        """Marks a point as smelly (don't allow robot suicide here).
        
        Args:
           x (int)
           y (int)

        """
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
        # list of lines to output
        out = []
        # for every robot, follow instructions
        for i in range(len(self.robots)):
            robot = self.robots[i]
            instructions = self.instructions[i]
            for instruction in instructions:
                if instruction == 'L':
                    robot.turn_left()
                elif instruction == 'R':
                    robot.turn_right()
                elif instruction == 'F':
                    # save current position so we can move back if needed
                    previous_position = robot.position
                    robot.move_forward()
                else:
                    raise ValueError("Invalid instruction")

                # if the robot is now outside of the grid....
                if not self.grid.coordinate_is_within_bounds(robot.position.x, robot.position.y):
                    # put the robot back in its previous position
                    robot.position = previous_position
                    if self.grid.suicide_allowed_at(robot.position.x, robot.position.y):
                        robot.die()
                        # mark current edge position as smelly
                        self.grid.mark_point_as_smelly(robot.position.x, robot.position.y)

        # generate output
        for robot in self.robots:
            info = []
            # x coordinate
            info.append(str(robot.position.x))
            # y coordinate
            info.append(str(robot.position.y))
            # orientation
            info.append(robot.get_orientation())
            # lost?
            if not robot.alive:
                info.append("LOST")
            out.append(" ".join(info))
        return out



def parse_commands(commands):
    """Parse the given instructions (separated by newlines)"""
    x, y = map(int, commands[0].split(" "))

    # if coordinate larger than 50, throw exception
    if x > 50 or y > 50:
        raise ValueError("Coordinate too large")

    # initialize simulation
    simulation = Simulation(x, y)

    parsing_robot = True
    for command in commands[1:]:
        # if more than 100 chars, throw exception
        if len(commands) > 100:
            raise ValueError("Instruction too long")
        # alternate between adding instructions and robots
        if parsing_robot:
            x, y, orientation = command.split(" ")
            simulation.robots.append(Robot(int(x), int(y), orientation))
        else:
            # this is a line with instructions for the current robot
            simulation.instructions.append(list(command))
        parsing_robot = not parsing_robot
    
    return simulation
    
def main():
    """Runs a simulation based on stdin input and outputs the results to stdout"""

    commands = []
    for line in sys.stdin:
        # ignore newlines
        if line != "\n":
            commands.append(line.rstrip("\n"))

    # Parse commands -> output will be a simulation object.
    simulation = parse_commands(commands)

    # Run simulation, print results to stdout.
    result = simulation.run()
    for line in result:
        print(line)

if __name__ == "__main__":
    # Will only be executed when this module is run directly.
    main()

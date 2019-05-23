#Mars Rover Problem


Description of Problem:
A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover's position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).
Input: 
The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.
The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.
The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.
Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.
Output: The output for each rover should be its final co-ordinates and heading.
 
Input and Output
Test Input:
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

Expected Output:
1 3 N
5 1 E


#Solution

Dependencies:
* Python3


Running and exercising code:

1. Pull all code, keeping file structure
2. Edit mission_instructions.txt to contain desired input. Make sure input format is correct.
3. In Terminal run command `python mission_instructions.py`
4. Test cases are ran using command `python mars_rover_tests.py`

Things to note:

There are some extra features to the system that I have implemented.

1. Any instruction that would cause the rover to either:
	a. Run into another stationary rover 
	b. Move beyond the boundaries of the Plateau
   results in a message being displayed to the user followed by abortion of the instruction and the rover changing it's direction by making one right turn. These messages are displayed along with the final location of the rovers. 

2. Any instruction entered that is not a valid instruction results in an error specifying the problem to the user and asking for correction.

3. Any attempt in trying to set a rover outside of the determined plateau is aborted and an error explains to the user that they must fix the attempted placement. 





# AI
COEN 266 Artificial Intelligence
Group Homework #1 Search
This is a GROUP assignment. The code for this assignment consists of several Python files, some of which
you will need to read and understand in order to complete the assignment, and some of which you can ignore.
You can download and unzip all the code and supporting files search_and_games.zip.
Files to Edit: You will edit portions of search.py, where all your search algorithms will reside. There is no
need to change the other files/code in the source code folder.
Submission:
1. Submit a pdf report to Camino (for the format of the pdf report, please refer to
GroupHW1_submission_sample.pdf).
2. Submit all source code needed (with search.py modified by you) to generate all results of the
Experiments in Problem 1 and Problem 2 as a .zip file to Camino. We will test run your submitted
code, so make sure it works.
The following items are essential components of your algorithm. Please explain them in the submitted pdf
report.
• For Breadth-First Search:
o How Frontier is defined
o How graph search is implemented
o How successors (children nodes) of the current node are generated and how they enter the
Frontier queue
o How goalTest is called
o How the solution path is returned
• For A* Search:
o How g, h, and f values are obtained for a node
o How Frontier is defined
o How graph search is implemented
o How successors (children nodes) of the current node are generated and how they enter the
Frontier queue
o How goalTest is called
o How the solution path is returned
Files you might want to look at
pacman.py The main file that runs Pacman games. This file describes a Pacman GameState class,
which you use in this project.
game.py The logic behind how the Pacman world works. This file describes several supporting
classes like AgentState, Agent, Direction, and Grid.
searchAgents.py Where all your search-based agents will reside.
util.py Useful data structures for implementing search algorithms.
Files you will not edit
agentTestClasses.py Autograding test classes
graphicsDisplay.py Graphics for Pacman
graphicsUtils.py Support for Pacman graphics
textDisplay.py ASCII graphics for Pacman
ghostAgents.py Agents to control ghosts
keyboardAgents.py Keyboard interfaces to control Pacman
layout.py Code for reading layout files and storing their contents
autograder.py Project autograder
testParser.py Parses autograder test and solution files
testClasses.py General autograding test classes
test_cases/ Directory containing the test cases for each question
Academic Dishonesty: We will be checking your code against other groups’ submissions in the class for
logical redundancy. If you copy someone else’s code and submit it with minor changes, we will know, and
we will pursue the strongest consequences available to us.
This assignment is adapted from the Pacman AI projects developed at UC Berkeley, http://ai.berkeley.edu.
Welcome to Pacman
After downloading the code (search_and_games.zip), unzipping it, and changing to the directory, you should
be able to play a game of Pacman by typing the following at the command line:
python pacman.py
Pacman lives in a shiny blue world of twisting corridors and tasty round treats. Navigating this world
efficiently will be Pacman's first step in mastering his domain.
The simplest agent in searchAgents.py is called the GoWestAgent, which always goes West (a trivial reflex
agent). This agent can win:
python pacman.py --layout testMaze --pacman GoWestAgent
But, things get ugly for this agent when turning is required:
python pacman.py --layout tinyMaze --pacman GoWestAgent
If Pacman gets stuck, you can exit the game by typing CTRL-c into your terminal.
Note that pacman.py supports a number of options that can each be expressed in a long way (e.g., --layout)
or a short way (e.g., -l). You can see the list of all options and their default values via:
python pacman.py -h
Also, all of the commands that appear in this portion of the project also appear in commands.txt, for easy
copying and pasting. 
Problem 1: Breadth-First Search
In the breadthFirstSearch function in search.py, implement the breadth-first graph search algorithm
(states/locations that are already visited will not be visited again), for Pacman to find the path to the dot in
the maze. You will probably want to make use of the Node class in search.py.
Experiments: Test your code using:
python pacman.py -l tinyMaze -p SearchAgent -a fn=breadthFirstSearch
python pacman.py -l smallMaze -p SearchAgent -a fn=breadthFirstSearch
python pacman.py -l mediumMaze -p SearchAgent -a fn=breadthFirstSearch -z .5 --frameTime 0
python pacman.py -l bigMaze -p SearchAgent -a fn=breadthFirstSearch -z .5 --frameTime 0
Problem 2: A* Search
Implement the A* graph search in the empty function aStarSearch in search.py, for Pacman to find the path
to the dot in the maze. You will probably want to make use of the Node class in search.py and the
PriorityQueue class in util.py.
You would need a heuristic function. Heuristics take two arguments: a state in the search problem (the main
argument), and the problem itself (for reference information). The nullHeuristic heuristic function in
search.py is a trivial example.
In your code, you can use the Manhattan distance heuristic (implemented already as manhattanHeuristic in
searchAgents.py).
Run the following experiments to test your code.
Experiments:
python pacman.py -l tinyMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
python pacman.py -l smallMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
python pacman.py -l mediumMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic --frameTi
me 0
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic --frameTime 0
A few additional notes:
• If Pacman moves too slowly for you, try the option --frameTime 0.
• All of your search functions need to return a list of actions that will lead the agent from the start to the
goal. 

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
pacman.py ->>>>>>>>The main file that runs Pacman games. This file describes a Pacman GameState class,
which you use in this project.

game.py->>>>>>> The logic behind how the Pacman world works. This file describes several supporting
classes like AgentState, Agent, Direction, and Grid.

searchAgents.py->>>>>> Where all your search-based agents will reside.
util.py Useful data structures for implementing search algorithms.

Files you will not edit

agentTestClasses.py ----->>Autograding test classes

graphicsDisplay.py ----->>Graphics for Pacman

graphicsUtils.py ---->Support for Pacman graphics

textDisplay.py ------->ASCII graphics for Pacman

ghostAgents.py-------> Agents to control ghosts

keyboardAgents.py ----->Keyboard interfaces to control Pacman

layout.py ------>Code for reading layout files and storing their contents

autograder.py ----->Project autograder

testParser.py ------->Parses autograder test and solution files

testClasses.py ------>General autograding test classes

test_cases/ ------->Directory containing the test cases for each question

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


=============

Introduction
COEN 266 Artificial Intelligence Group Homework #2 Minimax Game
In this GROUP assignment, you will design a minimax algorithm for Pacman (player-MAX), who plays a game with three ghosts (player-MINs). The game tree will have MAX nodes and MIN nodes. In general, MAX nodes will call a “max” function to collect the largest value from its successors, and MIN nodes will call a “min” function to collect the minimum value from its successors.
You can download and unzip all the code and supporting files from multiagent.zip. Implement the following function in Class MinimaxAgent, in multiAgents.py
def getAction(self, gameState):
...
# this function will
• recursively call a “max” function and a “min” function.
• propagate the “leaf” node values to upper layers, until the root node is reached. • finally, return the best action for player-max (Pacman) at the root node.
Files you’ll edit:
multiAgents.py Where your multi-agent search agent will reside.
Files you might want to look at:
pacman.py The main file that runs Pacman games. This file also describes a Pacman GameState class, which you will use extensively in this assignment.
game.py The logic behind how the Pacman world works. This file describes several supporting classes like AgentState, Agent, Direction, and Grid.
util.py Useful data structures for implementing search algorithms. You may find some functions defined here to be useful.
                  
 Supporting files you can ignore:
   graphicsDisplay.py graphicsUtils.py textDisplay.py ghostAgents.py keyboardAgents.py layout.py
Graphics for Pacman
Support for Pacman graphics
ASCII graphics for Pacman
Agents to control ghosts
Keyboard interfaces to control Pacman
Code for reading layout files and storing their contents
                  Task: Minimax Agent
 Now you will write an adversarial search agent in the provided   class stub
in multiAgents.py. Your minimax agent should work with any number of ghosts. In particular, your minimax tree will have multiple min layers (one for each ghost) for every max layer.
Your code should also expand the game tree to an arbitrary depth. Score the leaves of your minimax tree with the supplied . MinimaxAgent extends MultiAgentSearchAgent, which gives access to   (the number of search plies of the game tree). A single search ply (self.depth=1) is considered to be one Pacman move and all the ghosts’ responses, so a search with self.depth=2 will involve Pacman and each ghost moving two times.
    scoreEvaluationFunction
self.depth
MinimaxAgent
 Make sure your minimax code makes reference to variable self.depth where appropriate as this variable is populated in response to command line options.
Experiment:
  python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4 --frameTime 0 Hints and Observations
   • The evaluation function for the Pacman test in this part is already written (   ), which evaluates the states. You shouldn’t change this function.
• The minimax values of the initial state in the minimaxClassic layout are 9, 8, 7, -492 for self.depth=1, 2, 3 and 4 respectively.
• Pacman is always agent 0, and the agents move in order of increasing agent index.
• All states in minimax should be , either passed in to getAction or generated via .
   GameStates
 GameState.generateSuccessor
scoreEvaluationFunction

 openClassic
mediumClassic
• On larger boards such as   and   (the default), you’ll find Pacman to be good at not dying, but quite bad at winning. He’ll often thrash around without making progress. He might even thrash around right next to a dot without eating it because he doesn’t know where he’d go after eating that dot.
• You can check the correctness of your code by running the following test:
  • python autograder.py -q q2
• python autograder.py -q q2 --no-graphics
Submission:
1. Submit a pdf file to Camino (for the format of the file, please refer to GroupHW2_submission_sample.pdf).
The following items are essential components of your code, and you will explain them in your pdf report.
• How does the “max” function work?
• How does the “min” function work?
• How to recursively call the “max” function and “min” function?
• How is depth=4 reached?
• How does the root node return the best action?
• How do you set the PlayerIndex for Pacman and for three ghosts?
• When depth<4, how to go from the 3rd ghost to the next player-MAX, and at the same time increase
the depth by 1?
2. Submit all source code needed (with multiAgents.py modified by you) to generate the result of the Experiment as a .zip file to Camino. We will test run your submitted code, so make sure it works. We expect Pacman to win at least 5 out of 10 successive games. Your code should also pass 5/5 tests of the following: python autograder.py -q q2 --no-graphics
  • This will show what your algorithm does on a number of small trees, as well as a pacman game. To run it without graphics, use:
    • The correct implementation of minimax will lead to Pacman losing the game in some tests of the aforementioned autograder.py. This is not a problem: as it is correct behavior, it will pass the tests.

 ======

 COEN 266 Artificial Intelligence
Group Homework #3 Reinforcement Learning
This is a GROUP assignment. You will download rl.zip and modify the functions in
“class QLearningAgent(ReinforcementAgent):” of qlearningAgents.py
Task A: Implement a Q-learning agent to walk in the grid world we saw in class. The agent learns by trial and
error from interactions with the environment through its update(state, action, nextState, reward) method. A
stub of a Q-learner is specified in QLearningAgent in qlearningAgents.py, and you can select it with the
option '-a q'.
You will implement the update, computeValueFromQValues, getQValue,
and computeActionFromQValues functions in qlearningAgents.py.
Note: For computeActionFromQValues, you should break ties randomly for better behavior.
The random.choice() function will help. In a particular state, actions that your agent hasn’t seen before still
have a Q-value, specifically a Q-value of zero.
Important: Make sure that in your computeValueFromQValues and computeActionFromQValues functions,
you only access Q values by calling getQValue.
Task A – Experiment 1 With the Q-learning update in place, you can watch your Q-learner learn under
manual control, using the keyboard:
python gridworld.py -a q -k 4 -m --noise 0.0
Note: -k will control the number of episodes your agent gets to learn, -m means you manually control Pacman’s
actions, and --noise 0.0 means there is no randomness (it’s a deterministic game). Please manually steer
Pacman north and then east along the optimal path for four episodes, and you should see the following updated
Q-values:
Hint:
• In computeValueFromQValues and computeActionFromQValues, the available actions shall be
obtained by: self.getLegalActions(state)
• Watch how the agent learns about the state it was just in, not the one it moves to.
In the pdf report, show the screen shot of the above final result (gridworld with updated Q-state values) after
4 manual episodes are executed.
Task A – Experiment 2 Run the command:
python autograder.py -q q3
Your code is expected to pass all four test_cases of the above command.
In the pdf report, show the screen shot of the result showing that your code has passed all four test_cases.
Task B: Keep the modified code in Task A. Now, you will continue to modify the “def getAction(self, state):”
function in the same qlearningAgents.py file. This function computes the action to take in the current state.
There is a parameter self.epsilon, which is a probability. With probability self.epsilon, the agent should take a
random action of all legal actions available in that state. With probability 1- self.epsilon, the agent will take
the best policy action obtained by the computeActionFromQValues function.
Task B – Experiment 1 Run the following command, and observe how the Q-learner updates the Q-state values
for 100 episodes.
python gridworld.py -a q -k 100
In the pdf report, show the screen shot of the final result (gridworld with updated Q-state values) after 100
automatic episodes are executed.
Task B – Experiment 2 Run the following command and observe how the crawler bot learns to move to the
right. You can decrease the “Step Delay” to 0.0125 by pressing the top-left “-” button, so that you will see the
displayed results sooner.
python crawler.py
In the pdf report, show the screen shot of the intermediate result of your code (when the crawler bot is in the
middle of the scene)
Task B – Experiment 3 Run the following autograder, and you code should pass all four test_cases.
python autograder.py -q q4
In the pdf report, show the screen shot of the result showing that your code has passed all four test_cases.
Submission:
1. Submit a pdf file to Camino.
• Explain how you implemented the following functions in your qlearningAgents.py code, with code
snippets. (These functions are essential components of your algorithm.)
▪ getQValue
▪ computeValueFromQValues
▪ computeActionFromQValues
▪ update
▪ getAction
• For each experiment, include a screen shot/picture of the required results specified earlier in this
document (in blue).
2. Submit all source code needed (with qlearningAgents.py modified by you) to generate the results of all
Experiments in Tasks A and B as a .zip file to Camino. We will test run your submitted code, so make
sure it works. 

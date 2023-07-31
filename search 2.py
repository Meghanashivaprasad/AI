# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sys
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def goalTest(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
        Given a state, returns available actions.
        Returns a list of actions
        """        
        util.raiseNotDefined()

    def getResult(self, state, action):
        """
        Given a state and an action, returns resulting state.
        """
        util.raiseNotDefined()

    def getCost(self, state, action):
        """
        Given a state and an action, returns step cost, which is the incremental cost 
        of moving to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

class Node:
    """
    Search node object for your convenience.

    This object uses the state of the node to compare equality and for its hash function,
    so you can use it in things like sets and priority queues if you want those structures
    to use the state for comparison.

    Example usage:
    >>> S = Node("Start", None, None, 0)
    >>> A1 = Node("A", S, "Up", 4)
    >>> B1 = Node("B", S, "Down", 3)
    >>> B2 = Node("B", A1, "Left", 6)
    >>> B1 == B2
    True
    >>> A1 == B2
    False
    >>> node_list1 = [B1, B2]
    >>> B1 in node_list1
    True
    >>> A1 in node_list1
    False
    """
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state == other.state

    def __ne__(self, other):
        return self.state != other.state


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.

    You are not required to implement this, but you may find it useful for Q5.
    """
    "*** YOUR CODE HERE ***"

    # Import the Queue class from the util module
    from util import Queue

    # Initialize an empty queue called frontier_nodes
    frontier_nodes = Queue()

    # Push the starting state and an empty list of actions to the queue
    frontier_nodes.push(
        {
            "state": problem.getStartState(),
            "actions": []
        }
    )

    # Initialize an empty dictionary called visited_nodes to keep track of nodes that have been explored
    visited_nodes= {}

    # While the frontier_nodes queue is not empty
    while frontier_nodes:
        # Pop the node from the front of the queue
        state = frontier_nodes.pop()

        # Check if the current state is the goal state
        if problem.goalTest(state["state"]):
            # If it is, return the list of actions that led to the goal state
            return state["actions"]

        # If the state has already been visited, skip to the next iteration of the loop
        if state["state"] in visited_nodes:
            continue

        # Mark the current state as visited
        visited_nodes[state["state"]] = 1

        # For each possible action from the current state
        for action in problem.getActions(state["state"]):
            # Get the resulting state from taking the action
            result = problem.getResult(state["state"], action)

            # Push the resulting state and the actions that led to it to the queue
            frontier_nodes.push(
                {
                    "state": result,
                    "actions": state["actions"] + [action]
                }
            )

    # If no goal state is found, return an empty list
    return []


    
def depthFirstSearch(problem): 

    "*** YOUR CODE HERE ***"   
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def iterativeDeepeningSearch(problem):
    """
    Perform DFS with increasingly larger depth. Begin with a depth of 1 and increment depth by 1 at every step.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.goalTest(problem.getStartState()))
    print("Actions from start state:", problem.getActions(problem.getStartState()))

    Then try to print the resulting state for one of those actions
    by calling problem.getResult(problem.getStartState(), one_of_the_actions)
    or the resulting cost for one of these actions
    by calling problem.getCost(problem.getStartState(), one_of_the_actions)

    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    
def UniformCostSearch(problem):
    """Search the node that has the lowest path cost first."""
    "*** YOUR CODE HERE ***"  
    util.raiseNotDefined()
    

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # Import the PriorityQueue class from the util module
    from util import PriorityQueue

    # Create a priority queue for frontier nodes
    frontier_nodes = PriorityQueue()

    # Push the start state of the problem onto the frontier, with a priority of 0
    frontier_nodes.push(
        {
            "state": problem.getStartState(),  # Get the starting state of the problem
            "actions": []  # Initialize the list of actions taken to reach this state as empty
        },
        0  # Priority is 0
    )

    # Initialize a dictionary to keep track of visited nodes
    visited_nodes = {}
    
    # While there are still nodes in the frontier
    while frontier_nodes:
        # Pop the node with the highest priority (lowest cost) from the frontier
        current_state = frontier_nodes.pop()

        # If the current state is a goal state, return the actions taken to reach it
        if problem.goalTest(current_state["state"]):
            return current_state["actions"]

        # If the current state has already been visited, continue to the next iteration
        if current_state["state"] in visited_nodes:
            continue

        # Mark the current state as visited
        visited_nodes[current_state["state"]] = 1

        # For each possible action from the current state
        for action in problem.getActions(current_state["state"]):
            # Get the resulting state of taking the action
            child = problem.getResult(current_state["state"], action)

            # Add the current action to the list of actions taken to reach this state
            actions = current_state["actions"] + [action]

            # Calculate the cost of taking these actions to reach the resulting state, including the heuristic cost
            cost = problem.getCostOfActions(actions) + heuristic(child, problem)

            # Push the resulting state onto the frontier, with the calculated cost as the priority
            frontier_nodes.push(
                {
                    "state": child,  # Resulting state
                    "actions": actions  # List of actions taken to reach this state
                },
                cost  # Priority is the cost of reaching this state
            )

    # If there are no more nodes in the frontier, return an empty list
    return []


# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ids = iterativeDeepeningSearch

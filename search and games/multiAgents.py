# multiAgents.py
# --------------
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


# multiAgents.py
# --------------
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


import random

import util
from game import Agent, Directions
from util import manhattanDistance


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        legalMoves = gameState.getLegalActions()
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        currentGameState: The current search state

        action: Direction; The action taken

        returns: float; a heuristic for the given (state,action) pair

        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        
        score = successorGameState.getScore()

        foodList = newFood.asList()
        if foodList:
            foodDistances = [util.manhattanDistance(newPos, food) for food in foodList]
            closestFood = min(foodDistances)
            score += 10.0 / (closestFood + 1)

        for ghostState, scaredTime in zip(newGhostStates, newScaredTimes):
            ghostDist = util.manhattanDistance(newPos, ghostState.getPosition())
            if scaredTime == 0:
                if ghostDist <= 1:
                    score -= 500
                else:
                    score -= 1.0 / ghostDist

        for ghostState, scaredTime in zip(newGhostStates, newScaredTimes):
            ghostDist = util.manhattanDistance(newPos, ghostState.getPosition())
            if scaredTime > 0:
                score += 2.0 / (ghostDist + 1)

        return score

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent & AlphaBetaPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 7)
    """

    def getAction(self, gameState):
        """
        gameState: the current state

        returns: Direction; the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        legalMoves = gameState.getLegalActions(0)
        bestScore = float('-inf')
        bestAction = None
        visitedStates = set()

        for action in legalMoves:
            successorState = gameState.generateSuccessor(0, action)
            score = self.minimax(successorState, 1, self.depth, visitedStates)  # Start from the ghost's turn (agent 1)
            if score > bestScore:
                bestScore = score
                bestAction = action

        return bestAction

    def minimax(self, gameState, agentIndex, depth, visitedStates):
        """
        Recursively calculates the minimax value for the current game state.
        """
        state_expansion_count = [0]
        state_expansion_count[0] += 1
        if depth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        if agentIndex == 0:
            bestScore = float('-inf')
            legalMoves = gameState.getLegalActions(agentIndex)
            for action in legalMoves:
                successorState = gameState.generateSuccessor(agentIndex, action)
                score = self.minimax(successorState, 1, depth, state_expansion_count)  # Ghosts' turn
                bestScore = max(bestScore, score)
            return bestScore
        else:
            bestScore = float('inf')
            legalMoves = gameState.getLegalActions(agentIndex)
            nextAgentIndex = (agentIndex + 1) % gameState.getNumAgents()
            nextDepth = depth - 1 if nextAgentIndex == 0 else depth

            for action in legalMoves:
                successorState = gameState.generateSuccessor(agentIndex, action)
                score = self.minimax(successorState, nextAgentIndex, nextDepth, state_expansion_count)
                bestScore = min(bestScore, score)

            return bestScore
        


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 8)
    """

    def getAction(self, gameState):
        """
        gameState: the current state

        returns: Direction; the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        legalMoves = gameState.getLegalActions(0)
        bestScore = float('-inf')
        bestAction = None

        for action in legalMoves:
            successorState = gameState.generateSuccessor(0, action)
            score = self.expectimax(successorState, 1, self.depth)
            if score > bestScore:
                bestScore = score
                bestAction = action

        return bestAction

    def expectimax(self, gameState, agentIndex, depth):
        """
        Recursively calculates the expectimax value for the current game state.
        """
        if depth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        legalMoves = gameState.getLegalActions(agentIndex)
        if not legalMoves:
            return self.evaluationFunction(gameState)

        if agentIndex == 0:
            return max(self.expectimax(gameState.generateSuccessor(agentIndex, action), 1, depth) for action in legalMoves)
        else:
            nextAgentIndex = (agentIndex + 1) % gameState.getNumAgents()
            nextDepth = depth - 1 if nextAgentIndex == 0 else depth
            return sum(self.expectimax(gameState.generateSuccessor(agentIndex, action), nextAgentIndex, nextDepth) for action in legalMoves) / len(legalMoves)


def betterEvaluationFunction(currentGameState):
    """
    currentGameState: the current state

    returns: float; the evaluation of the state

    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 9).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    pacmanPos = currentGameState.getPacmanPosition()
    foodList = currentGameState.getFood().asList()
    ghostStates = currentGameState.getGhostStates()
    capsules = currentGameState.getCapsules()

    score = currentGameState.getScore()

    if foodList:
        minFoodDist = min(manhattanDistance(pacmanPos, food) for food in foodList)
        score += 10.0 / minFoodDist
    for ghost in ghostStates:
        ghostPos = ghost.getPosition()
        ghostDist = manhattanDistance(pacmanPos, ghostPos)
        scaredTimer = ghost.scaredTimer

        if scaredTimer > 0:
            score += 15.0 / (ghostDist + 1)
        else:
            if ghostDist < 2:
                score -= 200
            else:
                score -= 5.0 / (ghostDist + 1)

    if capsules:
        minCapsuleDist = min(manhattanDistance(pacmanPos, cap) for cap in capsules)
        score += 20.0 / (minCapsuleDist + 1)

    return score

# Abbreviation
better = betterEvaluationFunction


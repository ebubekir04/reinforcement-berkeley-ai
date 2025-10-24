# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        for z in range(self.iterations):  # aantal vereiste iteraties
            new_values = {}

            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state): # niks meer te winnen na een terminal state
                    new_values[state] = 0
                else:
                    bestq_value = float('-inf')
                    for action in self.mdp.getPossibleActions(state):
                        Q = self.computeQValueFromValues(state, action)
                        if bestq_value < Q:
                            bestq_value = Q  # Update Bestq_value als een grotere waarde gevonden is
                    new_values[state] = bestq_value  # Update de waarde van de toestand

            self.values = new_values  # update de waarden na elke iteratie

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"

        Q = 0
        paren = self.mdp.getTransitionStatesAndProbs(state, action)  # lijst van tuples (state, action), kans dat  volgendetoestande bereikt wordt na uitvoeren actie
        for nextstate, probability in paren:  # tuple concept
                beloning = self.mdp.getReward(state, action, nextstate)
                Vs = self.values[nextstate]  # waarden van de states die in het self.values object zitten
                total = probability * (beloning + self.discount * Vs)
                Q += total
        return Q


        # deze eerst
        # \sum_s{T(s,a,s')[R(s,a,s'] + \gamma V^*(S)]}
        # gamma is discount, zelf instellen
        # mdp.getStates()
        # mdp.getPossibleActions(state)
        # mdp.getTransitionStatesAndProbs(state, action)
        # mdp.getReward(state, action, nextState)
        # mdp.isTerminal

        self.mdp.getTransitionStatesAndProbs(state, action)
        self.mdp.getReward(state, action, ...)
        self.mdp.isTerminal(...)


        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"

        q = float("-inf")
        best_action = None

        for action in self.mdp.getPossibleActions(state):
            x = self.computeQValueFromValues(state, action)
            if x > q:
                q = x
                best_action = action

        return best_action

        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

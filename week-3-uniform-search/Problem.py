class Problem:
    def __init__(self, initial_state, goal_state):
        """
        Constructs a new problem instance with the given initial state and goal state.
        """
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        """
        Returns a list of valid actions that can be taken from the given state.
        This method needs to be implemented by a subclass of Problem.
        """
        raise NotImplementedError

    def result(self, state, action):
        """
        Applies the given action to the given state and returns the resulting state.
        This method needs to be implemented by a subclass of Problem.
        """
        raise NotImplementedError

    def goal_test(self, state):
        """
        Returns True if the given state is the goal state for this problem instance.
        """
        return state == self.goal_state

    def path_cost(self, c, state1, action, state2):
        """
        Returns the cost of the path that goes from state1 to state2 via the given action.
        For most problems, this cost is 1
        """

        return c + 1

 
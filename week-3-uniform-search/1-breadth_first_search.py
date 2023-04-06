
from Problem import Problem
from collections import deque

class PuzzleProblem(Problem):
    def __init__(self, initial_state, goal_state):

        super().__init__(initial_state, goal_state)

        self.width = 3
        self.height = 3

    
    def actions(self, state):

        # returns a list of valid actions that can be taken from a given state

        actions = []

        blank_idx = state.index(None) # get the index of the empty tile in the state
        
        row, col = divmod(blank_idx, self.width) # returns the coordinate of the blank index

        # for example if the blank index is at [1, 2, 0] -> divmod(2, 3) -> 2/3 = 0, 2%3 = 2 (because two cannot go to 3, so still 2 is remaining)

        # if it is not the first row
        if row > 0:
            actions.append("up")
        
        # if it is the bottom row or the middle row move down
        if row < self.height - 1:
            actions.append("down")

        # if the column is not the left column
        if col > 0:
            actions.append('left')

        # if the column is not the right column
        if col < self.width - 1:
            actions.append("right")

        print(f"state is {state} and have possible actions: {actions} ")
        return actions
    
    def result(self, state, action):

        # applies a given state and an action genereate a list of states 

        # find the blank index at the state and change its position based on the action given

        blank_idx = state.index(None)
        row, col = divmod(blank_idx, self.width)

        if action == "up":
            row -= 1
        elif action == "down":
            row += 1
        elif action == "left":
            col -= 1
        elif action == "right":
            col += 1

        else:
            raise ValueError(f"Invalid action: {action}")

        new_idx = row * self.width + col

        # because this is called recusively, it remembers its variables

        new_state = state.copy()

        new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]  # swap the tiles

        print(f"applied {action} which made state {new_state}")

        return new_state
                    


def Breadth_first_search(problem:Problem):

    """
    Breadth first search is a simple strategy in which the root is expanded first, then all of the sucessor of the root is expanded next, and
    then all of their sucessors and so on. 

    It uses FIFO queue (First in, First Out) for frontier.
    New nodes which are deeper than their parents goes to the back of the queue. 
    Old ones which are shallower than the new nodes, get expanded first.

    The time complexity of BFS is O(n^d) where n is the number of nodes and d = depth

    When the path cost is the same we can use this.

    """

    # initialise the frontier with intial state
    # it is using a queue data structure which is LIFO
    # the last element goes in, the first element comes out

    frontier = deque([(problem.initial_state, [])])

    # initialise the explored set
    explored = set()

    # continue searching until the frontier is empty

    while frontier:
        
        state, path = frontier.popleft()

        # check if state is the goal state
        if problem.goal_test(state):
            return path + [state]
        
        # add the state to the explored set, tuple state converts [1, 2] to (1,2 )
        explored.add(tuple(state))

        # generate successors of the state and add them to the frontier 
        for action in problem.actions(state):
            successor = problem.result(state, action)
            if tuple(successor) not in explored:
                new_path = path + [action]
                frontier.append((successor, new_path))

    # if the goal state was not found at all
    return None



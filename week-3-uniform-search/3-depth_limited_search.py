from Node import Node

def depth_limited_search(problem, limit):
    # Start the search by calling the recursive DLS function on the initial state
    return recursive_dls(Node(problem.initial_state), problem, limit)

def recursive_dls(node, problem, limit):
    # Check if the current node contains a goal state
    if problem.goal_test(node.state):
        return node.solution()
    # Check if the depth limit has been reached
    elif limit == 0:
        return "cutoff"
    else:
        cutoff_occurred = False
        # Expand the current node by generating its child nodes
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            result = recursive_dls(child, problem, limit - 1)
            # Check if a cutoff occurred in the recursive call
            if result == "cutoff":
                cutoff_occurred = True
            # Check if a solution was found
            elif result is not None:
                return result
        # Return cutoff if it occurred, otherwise failure
        if cutoff_occurred:
            return "cutoff"
        else:
            return None


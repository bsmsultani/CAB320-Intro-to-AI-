import heapq
from Node import Node
from Problem import Problem


def uniform_cost_search(problem: Problem):
    node = (problem.initial_state, problem.initial_state.path_cost)
    frontier = [(0, node)]
    explored = set()
    
    while frontier:
        _, node = heapq.heappop(frontier)
        if problem.goal_test(node[0]):
            return node[0]
        explored.add(node[0])
        
        for action in problem.actions(node[0]):
            child_state = problem.result(node[0], action)
            child_node = (child_state, node[1] + problem.step_cost(node[0], action))
            if child_state not in explored:
                heapq.heappush(frontier, (child_node[1], child_node))
            elif any(item[1][0] == child_state and item[1][1] > child_node[1] for item in frontier):
                heapq.heappush(frontier, (child_node[1], child_node))
    
    return None

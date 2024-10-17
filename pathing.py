import graph_data
import global_game_data
from numpy import random
from collections import deque

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    path = []
    exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
    target = global_game_data.target_node[global_game_data.current_graph_index]
    target_hit = False
    curr_node = 0

    # pre conditions
    assert is_valid_graph(graph_data.graph_data[global_game_data.current_graph_index]), 'Graph is not valid'
    assert all(len(graph_data.graph_data[global_game_data.current_graph_index]) > node for node in [curr_node, exit_node, target]), 'Exit, start, target node not all in graph range'

    while (curr_node != exit_node) or (target_hit == False):
        adjacent_nodes = graph_data.graph_data[global_game_data.current_graph_index][curr_node][1]
        curr_node = random.choice(adjacent_nodes)
        path.append(int(curr_node))
        if (curr_node == target):
            target_hit = True

    # post conditions
    assert nodes_in_path_are_adjacent(path, graph_data.graph_data[global_game_data.current_graph_index]), 'Not all adjacent nodes in path are adjacent in graph'
    assert path[0] in graph_data.graph_data[global_game_data.current_graph_index][0][1], 'Path does not begin at start'
    assert target in path, 'Target never hit in path'
    assert path[len(path) - 1] == exit_node, 'Path does not end at exit node'

    return path


def get_dfs_path():

        path = []
        exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
        target = global_game_data.target_node[global_game_data.current_graph_index]
        checkpoint_nodes = [target, exit_node]
        start_node = 0

        for checkpoint_node in checkpoint_nodes:

            frontier = []
            frontier.append(start_node)

            visited = set()
            visited.add(start_node)

            parents = {}
            parents[start_node] = None

            while frontier:
                current = frontier.pop()

                if current == checkpoint_node:
                    break

                neighbors = graph_data.graph_data[global_game_data.current_graph_index][current][1]

                for neighbor in neighbors:

                    if neighbor not in visited:
                        visited.add(neighbor)
                        parents[neighbor] = current
                        frontier.append(neighbor)
            
            current = checkpoint_node
            run = []
            while current is not None:
                run.append(current)
                current = parents[current]

            run.pop()
            path.extend(reversed(run))
            start_node = target

        return path


def get_bfs_path():

        path = []
        exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
        target = global_game_data.target_node[global_game_data.current_graph_index]
        checkpoint_nodes = [target, exit_node]
        start_node = 0

        for checkpoint_node in checkpoint_nodes:

            frontier = deque()
            frontier.append(start_node)

            visited = set()
            visited.add(start_node)

            parents = {}
            parents[start_node] = None

            while frontier:
                current = frontier.popleft()

                if current == checkpoint_node:
                    break

                neighbors = graph_data.graph_data[global_game_data.current_graph_index][current][1]

                for neighbor in neighbors:

                    if neighbor not in visited:
                        visited.add(neighbor)
                        parents[neighbor] = current
                        frontier.append(neighbor)
            
            current = checkpoint_node
            run = []
            while current is not None:
                run.append(current)
                current = parents[current]

            run.pop()
            path.extend(reversed(run))
            start_node = target

        # post conditions
        assert nodes_in_path_are_adjacent(path, graph_data.graph_data[global_game_data.current_graph_index]), 'Not all sequential vertices in the path are connected by an edge'
        assert path[0] in graph_data.graph_data[global_game_data.current_graph_index][0][1], 'Path does not begin at start'
        assert target in path, 'Target never hit in path'
        assert path[len(path) - 1] == exit_node, 'Path does not end at exit node'

        return path


def get_dijkstra_path():
    return [1,2]

def nodes_in_path_are_adjacent(path, graph):
    for i in range(len(path) - 2):
        curr_node = path[i]
        adjacent_nodes = graph[curr_node][1]
        next_node = path[i + 1]
        if next_node not in adjacent_nodes:
            return False
    return True


def is_valid_graph(graph):
    # graph is a list
    if not isinstance(graph, list):
        return False

    for node_data in graph:
        # each node in graph is represented by a list of length 2
        if not isinstance(node_data, list) or len(node_data) != 2:
            return False
        
        # coordinates are tuple with 2 numerical values
        if not isinstance(node_data[0], tuple) or len(node_data[0]) != 2 or not all(isinstance(value, (int, float)) for value in node_data[0]):
            return False

        # adjacency list is list of integers
        if not isinstance(node_data[1], list) or not all(isinstance(neighbor, int) for neighbor in node_data[1]):
            return False
              
    return True
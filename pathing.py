import graph_data
import global_game_data
from numpy import random

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
    while (curr_node != exit_node) or (target_hit == False):
        adjacent_nodes = graph_data.graph_data[global_game_data.current_graph_index][curr_node][1]
        curr_node = random.choice(adjacent_nodes)
        path.append(int(curr_node))
        if (curr_node == target):
            target_hit = True
    # pre- and postconditions
    # nodes are connecting
    # method to validate graph, assert that is validate graph
    assert nodes_in_path_are_adjacent(path, graph_data.graph_data[global_game_data.current_graph_index]), 'Not all nodes in path are adjacent in graph'
    assert path[0] in graph_data.graph_data[global_game_data.current_graph_index][0][1], 'Path does not begin at start'
    assert target in path, 'Target not hit'
    assert path[len(path) - 1] == exit_node, 'Path does not end at exit node'
    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]

def nodes_in_path_are_adjacent(path, graph):
    for i in range(len(path) - 2):
        curr_node = path[i]
        print(curr_node)
        adjacent_nodes = graph[curr_node][1]
        next_node = path[i + 1]
        if next_node not in adjacent_nodes:
            return False
    return True
        

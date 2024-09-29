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
    exit_node = graph_data.graph_data[global_game_data.current_graph_index][len(graph_data.graph_data[global_game_data.current_graph_index])-1][1][0]
    target = global_game_data.target_node[global_game_data.current_graph_index]
    next_node= -1
    curr_node = 0
    target_hit = False
    while (next_node != exit_node) or (target_hit == False):
        adjacent_nodes = graph_data.graph_data[global_game_data.current_graph_index][curr_node][1]
        next_node = random.choice(adjacent_nodes)
        path.append(next_node)
        if (next_node == target):
            target_hit = True
        curr_node = next_node
    path.append(curr_node)
    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]

import graph_data
import global_game_data
import math

def get_f_w_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    exit_node = len(graph) - 1
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]

    parents = get_f_w(graph)
    segment_1 = get_path_segment(parents, start_node, target_node)[1:-1]
    segment_2 = get_path_segment(parents, target_node, exit_node)
    path = segment_1 + segment_2

    return path

def get_f_w(graph):
    matrix_size = len(graph)
    weights = [[float('inf')] * matrix_size for _ in range(matrix_size)]
    parents = [[None] * matrix_size for _ in range(matrix_size)]

    # get weights matrix
    for node in range(matrix_size):
        weights[node][node] = 0
        for neighbor in graph[node][1]:
            distance = calculate_distance_between_two_adjacent_nodes(graph, node, neighbor)
            weights[node][neighbor] = distance
            parents[node][neighbor] = node

    # get floyd-warshall parents
    for k in range(matrix_size):
        for i in range(matrix_size):
            for j in range(matrix_size):
                if weights[i][k] + weights[k][j] < weights[i][j]:
                    weights[i][j] = weights[i][k] + weights[k][j]
                    parents[i][j] = parents[k][j]

    return parents

def get_path_segment(parents, start_node, end_node):
    path = []
    path.append(end_node)

    while end_node != start_node:
        end_node = parents[start_node][end_node]
        path.append(end_node)

    path.reverse()
    return path

def calculate_distance_between_two_adjacent_nodes(graph, node_1, node_2):
    current_node = graph[node_1][0]
    next_node = graph[node_2][0]
                                                                                   
    distance = math.sqrt(math.pow(current_node[0] - next_node[0], 2) + math.pow(current_node[1] - next_node[1], 2))

    return distance
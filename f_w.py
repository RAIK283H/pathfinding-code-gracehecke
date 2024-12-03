import graph_data
import global_game_data
import math

# def get_f_w_path():
#     path = []
#     exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
#     start_node = 0
#     target = global_game_data.target_node[global_game_data.current_graph_index]
#     checkpoint_nodes = [target, exit_node]

#     for checkpoint_node in checkpoint_nodes:
#         parents = get_f_w()
#         path.append(exit_node)
#         z = parents[start_node][exit_node]
#         while z is not None:
#             path.append(z)
#             z = parents[start_node][z]
#         path.reverse()

#         current = checkpoint_node
#         run = []
#         while current is not None:
#             run.append(current)
#             current = parents[current][0]

#         run.pop()
#         path.extend(reversed(run))
#         start_node = target

#     return path

def get_f_w_path():
    path = []  # Final path to return
    exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
    start_node = 0
    target = global_game_data.target_node[global_game_data.current_graph_index]
    checkpoint_nodes = [target, exit_node]

    parents = get_f_w()  # Get the shortest path parent matrix

    for checkpoint_node in checkpoint_nodes:
        # Backtrack from exit_node to start_node using the parents matrix
        current_path = []
        current = exit_node

        # Backtrack until the start node is reached
        while current != start_node:
            current_path.append(current)
            current = parents[start_node][current]
            if current is None:  # No path exists
                break

        # If a valid path exists, add the start node and reverse the path
        if current is not None:
            current_path.append(start_node)
            current_path.reverse()
            path.extend(current_path[1:])  # Avoid repeating the start node

        # Now, repeat the process from the checkpoint node
        start_node = checkpoint_node  # Update start_node for next checkpoint

    return path

      
def get_f_w():
    weights = get_weights_matrix()
    parents = [[None for _ in range(len(weights))] for _ in range(len(weights))]
    for k in range(len(weights)):
        for i in range(len(weights)):  
            for j in range(len(weights)):
                if weights[i][k] != float('inf') and weights[k][j] != float('inf'):
                    if (weights[i][k] + weights[k][j]) < weights[i][j]:
                        weights[i][j] = weights[i][k] + weights[k][j]
                        parents[i][j] = k

    return parents

def get_weights_matrix():
    matrix_size = len(graph_data.graph_data[global_game_data.current_graph_index])
    weights = [[float('inf') for _ in range(matrix_size)] for _ in range(matrix_size)]

    for node in range(matrix_size):
        neighbors = graph_data.graph_data[global_game_data.current_graph_index][node][1]
        for neighbor in neighbors:
            distance = calculate_distance_between_two_adjacent_nodes(global_game_data.current_graph_index, node, neighbor)
            weights[node][neighbor] = distance

    return weights

def calculate_distance_between_two_adjacent_nodes(player_index, node_1, node_2):
    current_node = graph_data.graph_data[player_index][node_1][0]
    next_node = graph_data.graph_data[player_index][node_2][0]
                                                                                   
    distance = math.sqrt(math.pow(current_node[0] - next_node[0], 2) + math.pow(current_node[1] - next_node[1], 2))

    return distance

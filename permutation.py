import graph_data

def get_permutations(graph):
    all_permutations = []
    permutation = list(range(1, len(graph) - 1))
    all_permutations.append(permutation.copy())
    directions = [-1] * (len(graph) - 1)
    largest_mobile = get_largest_mobile_integer(permutation, directions)

    while largest_mobile is not None:
        permutation = swap_largest_mobile_integer(permutation, directions, largest_mobile)
        all_permutations.append(permutation.copy())
        directions = switch_directions(permutation, directions, largest_mobile)
        largest_mobile = get_largest_mobile_integer(permutation, directions)

    return all_permutations

def get_largest_mobile_integer(permutation, directions):
    largest_mobile = None

    for i in range(len(permutation)):
        dir = directions[i]
        adjacent_index = i + dir

        if 0 <= adjacent_index < len(permutation) and permutation[i] > permutation[adjacent_index]:
            if largest_mobile is None or permutation[i] > largest_mobile:
                largest_mobile = permutation[i]

    return largest_mobile

def swap_largest_mobile_integer(permutation, directions, largest_mobile):
    index = permutation.index(largest_mobile)
    dir = directions[index]
    swap_with = index + dir

    permutation[index], permutation[swap_with] = permutation[swap_with], permutation[index]
    directions[index], directions[swap_with] = directions[swap_with], directions[index]

    return permutation

def switch_directions(permutation, directions, largest_mobile):
    for i in range(len(permutation)):
        if permutation[i] > largest_mobile:
            directions[i] *= -1
    return directions

def get_hamiltonian_cycles(graph):
    all_permutations = get_permutations(graph)
    hamiltonian_cycles = []

    for permutation in all_permutations:
        if nodes_in_path_are_adjacent_including_edge_nodes(permutation, graph):
            hamiltonian_cycles.append(permutation.copy())

    if not hamiltonian_cycles:
         print('False')
         return False
    else:
        print(hamiltonian_cycles)
        return hamiltonian_cycles

def nodes_in_path_are_adjacent_including_edge_nodes(path, graph):
    for i in range(len(path) - 1):
        curr_node = path[i]
        adjacent_nodes = graph[curr_node][1]
        next_node = path[i + 1]
        if next_node not in adjacent_nodes:
            return False
        
    first_node = path[0]
    last_node = path[-1]
    if first_node not in graph[last_node][1]:
        return False
    
    return True

def main():
    for i in range(len(graph_data.sjt_sample_graph_data)):
        print('Graph at', i)
        get_hamiltonian_cycles(graph_data.sjt_sample_graph_data[i])

main()
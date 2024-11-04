
graph = [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1, 3]],
        [(200, -400), [2, 4]],
        [(200, -400), [3, 0]]
]

def get_permutations(graph):
    all_permutations = []
    permutation = list(range(1, len(graph)))
    all_permutations.append(permutation)
    directions = [-1] * (len(graph) - 1)
    largest_mobile = get_largest_mobile_integer(permutation, directions)

    while largest_mobile is not None:
        permutation = swap_largest_mobile_integer(permutation, directions, largest_mobile)
        all_permutations.append(permutation)
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

    # Swap the largest mobile integer with the adjacent element
    permutation[index], permutation[swap_with] = permutation[swap_with], permutation[index]
    directions[index], directions[swap_with] = directions[swap_with], directions[index]

    return permutation

def switch_directions(permutation, directions, largest_mobile):
    for i in range(len(permutation)):
        if permutation[i] > largest_mobile:
            directions[i] *= -1
    return directions

def main(graph):
    get_permutations(graph)

main(graph) 
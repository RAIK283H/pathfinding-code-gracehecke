
graph = [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1, 3]],
        [(200, -400), [2, 0]]    
]

def get_permutations(graph):
    permutation = list(range(1, len(graph)))
    directions = [-1] * len(graph)
    largest_mobile = get_largest_mobile_integer(permutation, directions)

    while largest_mobile is not None:
    
        permutation = swap_largest_mobile_integer(permutation, directions, largest_mobile)
        print(permutation)
        directions = switch_directions(permutation, directions, largest_mobile)
        largest_mobile = get_largest_mobile_integer(permutation, directions)

    print(directions)

def get_largest_mobile_integer(permutation, directions):
    largest_mobile = None

    for i in range(len(permutation)):
        # Get the direction of the current element (-1 for left, 1 for right)
        dir = directions[i]

        # Calculate the adjacent index in the current direction
        adjacent_index = i + dir

        # Check if the element can move (is within bounds and is larger than the adjacent element)
        if 0 <= adjacent_index < len(permutation) and permutation[i] > permutation[adjacent_index]:
            # Check if it’s the largest mobile integer found so far
            if largest_mobile is None:
                return largest_mobile
            if permutation[i] > largest_mobile:
                largest_mobile = permutation[i]

    return largest_mobile

def swap_largest_mobile_integer(permutation, directions, integer):
    largest_mobile_index = permutation.index(integer)
    largest_mobile_direction = directions[largest_mobile_index]
    # left
    if largest_mobile_direction == -1:
        permutation[largest_mobile_index] =  permutation[largest_mobile_index - 1]
        permutation[largest_mobile_index - 1] = integer
    elif largest_mobile_direction == 1:
        permutation[largest_mobile_index] =  permutation[largest_mobile_index + 1]
        permutation[largest_mobile_index + 1] = integer
    return permutation

def switch_directions(permutation, directions, integer):
    for i in range(len(permutation) - 1): 
        if permutation[i] > integer:
            if directions[i] == -1:
                directions[i] = 1
            elif directions[i] == 1:
                 directions[i] = -1
    return directions

def main(graph):
    get_permutations(graph)

main(graph) 
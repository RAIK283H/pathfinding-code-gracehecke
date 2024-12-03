import math
import unittest
import pathing
import global_game_data
import graph_data
import scoreboard
import permutation

class TestPathFinding(unittest.TestCase):

    def test_get_hamiltonian_cycles_with_larger_graph(self):
        graph = [
            [(0, 0), []],           
            [(1, 0), [2, 5]],             
            [(2, 0), [1, 3]],            
            [(3, 0), [2, 4, 7]],         
            [(4, 0), [3, 5]],            
            [(5, 0), [4, 6, 1]],             
            [(6, 0), []]            
        ]
        expected = [[1, 2, 3, 4, 5], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], 
                    [1, 5, 4, 3, 2], [3, 4, 5, 1, 2], [4, 3, 2, 1, 5], 
                    [5, 4, 3, 2, 1], [3, 2, 1, 5, 4], [2, 3, 4, 5, 1], 
                    [2, 1, 5, 4, 3]]

        actual = permutation.get_hamiltonian_cycles(graph)
        assert all(permutation in actual for permutation in expected), 'Does not return correct Hamiltonian cycles with larger graph'

    def test_get_hamiltonian_cycles_with_linear_graph(self):
        graph = [
            [(0, 0), [1]],          
            [(1, 0), [0, 2]],       
            [(2, 0), [1, 3]],       
            [(3, 0), [2, 4]],       
            [(4, 0), [3]]           
        ]
        expected = False
        actual = permutation.get_hamiltonian_cycles(graph)
        self.assertEqual(expected, actual, 'Does not return False for linear graph')

    def test_get_hamiltonian_cycles_with_three_nodes(self):
        graph = [
            [(0, 0), [1, 2]],     
            [(1, 0), [0, 2]],        
            [(2, 0), [0, 1]],   
        ]
        expected = False
        actual = permutation.get_hamiltonian_cycles(graph)
        self.assertEqual(expected, actual, 'Does not return False with three nodes')

    def test_get_hamiltonian_cycles_with_basic_cycle(self):
        graph = [
            [(0, 0), [1, 4]],      
            [(1, 0), [0, 2, 4, 3]],   
            [(2, 0), [1, 3]],      
            [(3, 0), [2, 4, 1]],     
            [(4, 0), [0, 1, 3]]    
        ]
        expected = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1], [2, 1, 3]]
        actual = permutation.get_hamiltonian_cycles(graph)
        self.assertEqual(expected, actual, 'Does not return correct hamiltonian for basic cycle')

    def test_nodes_in_path_are_adjacent_including_edge_nodes_with_edge_nodes_in_center(self):
        graph =     [
        [(0, 0), [1]],
        [(1, 1), [0, 2, 4]],
        [(0, 2), [1, 3]],
        [(2, 1), [2, 4]],
        [(2, 1), [3, 5, 1]],
        [(3, 1), [4]]
        ]
        path =  [3, 4, 1, 2]
        actual = permutation.nodes_in_path_are_adjacent_including_edge_nodes(path, graph)
        self.assertTrue(actual, 'Does not return proper value with edge nodes in center of permutation')

    def test_nodes_in_path_are_adjacent_including_edge_nodes_with_valid_path(self):
        graph =     [
        [(0, 0), [1]],
        [(1, 1), [0, 2, 3]],
        [(0, 2), [1, 3]],
        [(2, 1), [2, 4, 1]],
        [(3, 1), [3]]
        ]
        path =  [1, 2, 3]
        actual = permutation.nodes_in_path_are_adjacent_including_edge_nodes(path, graph)
        self.assertTrue(actual, 'Does not return True with connected edge nodes')

    def test_nodes_in_path_are_adjacent_including_edge_nodes_with_unconnected_edge_nodes(self):
        graph =     [
        [(0, 0), [1]],
        [(1, 1), [0, 2]],
        [(0, 2), [1, 3]],
        [(2, 1), [2, 4]],
        [(3, 1), [3]]
        ]
        path =  [1, 2, 3]
        actual = permutation.nodes_in_path_are_adjacent_including_edge_nodes(path, graph)
        self.assertFalse(actual, 'Does not return False with unconnected edge nodes')

    def test_nodes_in_path_are_adjacent_including_edge_nodes_with_invalid_path(self):
        graph =     [
        [(0, 0), [1]],
        [(1, 1), [0, 2]],
        [(0, 2), [1, 4]],
        [(2, 1), [4]],
        [(3, 1), [2, 3]]
        ]
        path =  [1, 2, 3]
        actual = permutation.nodes_in_path_are_adjacent_including_edge_nodes(path, graph)
        self.assertFalse(actual, 'Does not return False with invalid path')

    def test_switch_directions_right_swap(self):
        my_permutation = [1, 3, 2]
        directions = [1, -1, 1]
        largest_mobile = 3
        expected = [1, -1, 1]
        actual = permutation.switch_directions(my_permutation, directions, largest_mobile)
        self.assertEqual(expected, actual, "Directions not properly changed with right swap")

    def test_switch_directions_left_swap(self):
        my_permutation = [1, 2, 3]
        directions = [1, 1, -1]
        largest_mobile = 3
        expected = [1, 1, -1]
        actual = permutation.switch_directions(my_permutation, directions, largest_mobile)
        self.assertEqual(expected, actual, "Directions not properly changed with left swap")

    def test_swap_largest_mobile_integer_with_right_swap(self):
        my_permutation = [1, 3, 2]
        directions = [1, -1, 1]
        largest_mobile = 3
        expected = [3, 1, 2]
        actual = permutation.swap_largest_mobile_integer(my_permutation, directions, largest_mobile)
        self.assertEqual(expected, actual, "Largest mobile integer not properly swapped right")

    def test_swap_largest_mobile_integer_with_left_swap(self):
        my_permutation = [1, 2, 3]
        directions = [1, 1, -1]
        largest_mobile = 3
        expected = [1, 3, 2]
        actual = permutation.swap_largest_mobile_integer(my_permutation, directions, largest_mobile)
        self.assertEqual(expected, actual, "Largest mobile integer not properly swapped left")

    def test_get_largest_mobile_integer_with_all_right_direction(self):
        my_permutation = [1, 2, 3, 4]
        directions = [-1, -1, -1, -1]
        expected = 4
        actual = permutation.get_largest_mobile_integer(my_permutation, directions)
        self.assertEqual(expected, actual, "Largest mobile integer not returned in last index")

    def test_get_largest_mobile_integer_with_all_left_direction(self):
        my_permutation = [4, 3, 2, 1]
        directions = [1, 1, 1, 1]
        expected = 4
        actual = permutation.get_largest_mobile_integer(my_permutation, directions)
        self.assertEqual(expected, actual, "Largest mobile integer not returned in last index")

    def test_get_largest_mobile_integer_with_large_permutation(self):
        my_permutation = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        directions = [-1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1]
        expected = 12
        actual = permutation.get_largest_mobile_integer(my_permutation, directions)
        self.assertEqual(expected, actual, "Largest mobile integer not returned in last index")

    def test_get_largest_mobile_integer_in_last_index(self):
        my_permutation = [1, 2, 3]
        directions = [1, 1, -1]
        expected = 3
        actual = permutation.get_largest_mobile_integer(my_permutation, directions)
        self.assertEqual(expected, actual, "Largest mobile integer not returned in last index")

    def test_get_largest_mobile_integer_in_first_index(self):
        my_permutation = [3, 2, 1]
        directions = [1, 1, -1]
        expected = 3
        actual = permutation.get_largest_mobile_integer(my_permutation, directions)
        self.assertEqual(expected, actual, "Largest mobile integer not returned in first index")

    def test_get_largest_mobile_integer_with_no_mobile_integer(self):
        my_permutation = [2, 1, 3, 4]
        directions = [-1, -1, 1, 1]
        expected = None
        actual = permutation.get_largest_mobile_integer(my_permutation, directions)
        self.assertEqual(expected, actual, "Does not return None when no mobile integer left")

    def test_get_permutations_with_2_node_graph(self):
        graph =  [
        [(0, 0), [1]],
        [(200, -200), [0]]
        ]
        expected_permuations = [[]]
        actual_permutations = permutation.get_permutations(graph)
        self.assertEqual(expected_permuations, actual_permutations, "Incorrect permutations for 2 node graph")

    def test_get_permutations_with_3_node_graph(self):
        graph =  [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1]]
        ]
        expected_permuations = [[1]]
        actual_permutations = permutation.get_permutations(graph)
        self.assertEqual(expected_permuations, actual_permutations, "Incorrect permutations for 3 node graph")

    def test_get_permutations_with_4_node_graph(self):
        graph =  [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1, 3]],
        [(200, -400), [2]]
        ]
        expected_permuations = [[1, 2], [2, 1]]
        actual_permutations = permutation.get_permutations(graph)
        self.assertEqual(expected_permuations, actual_permutations, "Incorrect permutations for 4 node graph")
    
    def test_get_permutations_with_5_node_graph(self):
        graph =  [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1, 3, 4]],
        [(200, -400), [2, 4]],
        [(200, -400), [2, 3]]
        ]
        expected_permuations = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1], [2, 1, 3]]
        actual_permutations = permutation.get_permutations(graph)
        self.assertEqual(expected_permuations, actual_permutations, "Incorrect permutations for 5 node graph")

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def test_nodes_in_path_are_adjacent_with_valid_path(self):
        graph =     [
        [(0, 0), [1]],
        [(1, 1), [0, 2]],
        [(0, 2), [1, 4]],
        [(2, 1), [4]],
        [(3, 1), [2, 3]]
        ]
        path =  [1, 2, 4]
        pathing.nodes_in_path_are_adjacent(path, graph)
        self.assertTrue(pathing.nodes_in_path_are_adjacent(path, graph), 'Should return True with valid path.')

    def test_nodes_in_path_are_adjacent_with_invalid_path(self):
        graph =     [
        [(0, 0), [1]],
        [(1, 1), [0, 2]],
        [(0, 2), [1, 4]],
        [(2, 1), [4]],
        [(3, 1), [2, 3]]
        ]
        path =  [1, 2, 3, 4]
        pathing.nodes_in_path_are_adjacent(path, graph)
        self.assertFalse(pathing.nodes_in_path_are_adjacent(path, graph), 'Should return False with invalid path.')

    def test_nodes_in_path_are_adjacent_with_single_node_path(self):
        graph =     [
        [(0, 0), [1]],
        [(1, 1), [0, 2]],
        [(0, 2), [1, 4]]
        ]
        path =  [1]
        pathing.nodes_in_path_are_adjacent(path, graph)
        self.assertTrue(pathing.nodes_in_path_are_adjacent(path, graph), 'Should return True with valid single node path.')

    def test_is_valid_graph_with_valid_graph(self):
        graph = [
            [(0, 0), [1]],
            [(100, 100), [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertTrue(pathing.is_valid_graph(graph), "Should return True for a valid graph.")
        
    def test_is_valid_graph_graph_is_not_list(self):
        graph = (
            [(0, 0), [1]],
            [(100, 100), [0, 2]],
            [(200, 200), [1]]
        )
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when graph is not a list.")
        
    def test_is_valid_graph_node_data_is_not_list(self):
        graph = [
            ((0, 0), [1]),
            [(100, 100), [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when node_data is not a list.")
        
    def test_is_valid_graph_coordinates_are_not_tuple(self):
        graph = [
            ((0, 0), [1]),
            [[100, 100], [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when coordinates are not a tuple.")
        
    def test_is_valid_graph_adjacency_list_is_not_list(self):
        graph = [
            ((0, 0), 1),
            [(100, 100), [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when adjacency list is not a list.")
        
    def test_is_valid_graph_node_data_length_not_2(self):
        graph = [
            ((0, 0), 1),
            [(100, 100)],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when length of node_data is not 2.")

    def test_is_valid_graph_coordinates_length_not_2(self):
        graph = [
            [(0, 0), [1]],
            [(100, 100, 100), [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when length of coordinates is not 2.")
        
    def test_is_valid_graph_adjacency_list_not_ints(self):
        graph = [
            [(0, 0), [1, 1.5]],
            [(100, 100), [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when adjacency list does not contain only integers.")

    def test_is_valid_graph_coordinates_not_numerical(self):
        graph = [
            [(0, 0), [1]],
            [(1, '1'), [0, 2]],
            [(0, 2), [1, 4]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when coordinates contain non-numerical value.")

    def test_get_bfs_path_with_linear_path(self):
        graph_data.graph_data = [[
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2]]
        ]]
        global_game_data.target_node= [1]
        actual_path = pathing.get_bfs_path()
        expected_path = [1, 2, 3]
        self.assertEqual(actual_path, expected_path), "Incorrect BFS output with linear path"

    def test_get_dfs_path_with_linear_path(self):
        graph_data.graph_data = [[
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2]]
        ]]
        global_game_data.target_node= [1]
        actual_path = pathing.get_dfs_path()
        expected_path = [1, 2, 3]
        self.assertEqual(actual_path, expected_path), "Incorrect DFS output with linear path"

    def test_bfs_with_cycle(self):
        graph_data.graph_data = [[
            [(0, 0), [1]],
            [(50, -200), [0, 2]],
            [(50, -300), [1, 3]],
            [(200, -500), [2, 0]]
        ]]
        global_game_data.target_node = [1]
        actual_path = pathing.get_bfs_path()
        expected_path = [1, 2, 3]
        self.assertEqual(actual_path, expected_path, "Incorrect BFS output with cyclical path")

    def test_dfs_with_cycle(self):
        graph_data.graph_data = [[
            [(0, 0), [1]],
            [(50, -200), [0, 2]],
            [(50, -300), [1, 3]],
            [(200, -500), [2, 0]]
        ]]
        global_game_data.target_node = [1]
        actual_path = pathing.get_dfs_path()
        expected_path = [1, 2, 3]
        self.assertEqual(actual_path, expected_path, "Incorrect DFS output with cyclical path")

    def test_bfs_with_multiple_branches(self):
        graph_data.graph_data = [[
            [(0, 0), [1, 2]],     
            [(50, -200), [0, 3, 4]],
            [(50, -300), [0, 5, 6]], 
            [(200, -400), [1]],   
            [(250, -400), [1, 7]],  
            [(300, -400), [2]],   
            [(350, -400), [2, 7]],   
            [(400, -500), [4, 6]]     
        ]]
        global_game_data.target_node = [3]  
        actual_path = pathing.get_bfs_path()
        expected_path = [1, 3, 1, 4, 7]
        self.assertEqual(actual_path, expected_path, "BFS failed with a path containing multiple branches")

    def test_dfs_with_multiple_branches(self):
        graph_data.graph_data = [[
            [(0, 0), [1, 2]],     
            [(50, -200), [0, 3, 4]],
            [(50, -300), [0, 5, 6]], 
            [(200, -400), [1]],   
            [(250, -400), [1, 7]],  
            [(300, -400), [2]],   
            [(350, -400), [2, 7]],   
            [(400, -500), [4, 6]]     
        ]]
        global_game_data.target_node = [3]  
        actual_path = pathing.get_dfs_path()
        expected_path = [1, 3, 1, 4, 7]
        self.assertEqual(actual_path, expected_path, "DFS failed with a path containing multiple branches")

    def test_get_bfs_path_with_large_graph(self):
        graph_data.graph_data =  [[
            [(900, 0), [21, 22]],
            [(0, 300), [7, 19, 20]],
            [(100, 400), [9, 10, 20]],
            [(200, 0), [6, 8, 11, 22]],
            [(200, 200), [6, 7, 11, 12]],
            [(200, 500), [10, 21]],
            [(300, 100), [3, 4, 11, 20]],
            [(300, 300), [1, 4, 9, 12, 20]],
            [(400, 0), [3, 11, 22]],
            [(400, 300), [2, 7, 12, 13, 15]],
            [(400, 500), [2, 5, 13, 14, 15]],
            [(400, 100), [3, 4, 6, 8, 12, 16, 17]],
            [(400, 300), [4, 7, 9, 11, 15, 17]],
            [(400, 400), [9, 10, 15]],
            [(500, 500), [10, 18, 15]],
            [(600, 400), [9, 10, 12, 13, 14]],
            [(600, 0), [11, 17]],
            [(600, 200), [11, 12, 16, 18]],
            [(700, 400), [14, 17]],
            [(0, 500), [1, 8, 21]],
            [(0, 200), [1, 2, 6, 7, 22]],
            [(400, 700), [5, 19, 0]],
            [(0, 0), [0, 3, 20]]
        ]]
        global_game_data.target_node= [1]
        actual_path = pathing.get_bfs_path()
        expected_path = [21, 19, 1, 20, 22]
        self.assertEqual(actual_path, expected_path), "Incorrect BFS output with large graph"

    def test_get_dfs_path_with_large_graph(self):
        graph_data.graph_data =  [[
            [(900, 0), [21, 22]],
            [(0, 300), [7, 19, 20]],
            [(100, 400), [9, 10, 20]],
            [(200, 0), [6, 8, 11, 22]],
            [(200, 200), [6, 7, 11, 12]],
            [(200, 500), [10, 21]],
            [(300, 100), [3, 4, 11, 20]],
            [(300, 300), [1, 4, 9, 12, 20]],
            [(400, 0), [3, 11, 22]],
            [(400, 300), [2, 7, 12, 13, 15]],
            [(400, 500), [2, 5, 13, 14, 15]],
            [(400, 100), [3, 4, 6, 8, 12, 16, 17]],
            [(400, 300), [4, 7, 9, 11, 15, 17]],
            [(400, 400), [9, 10, 15]],
            [(500, 500), [10, 18, 15]],
            [(600, 400), [9, 10, 12, 13, 14]],
            [(600, 0), [11, 17]],
            [(600, 200), [11, 12, 16, 18]],
            [(700, 400), [14, 17]],
            [(0, 500), [1, 8, 21]],
            [(0, 200), [1, 2, 6, 7, 22]],
            [(400, 700), [5, 19, 0]],
            [(0, 0), [0, 3, 20]]
        ]]
        global_game_data.target_node= [1]
        actual_path = pathing.get_dfs_path()
        expected_path = [22, 20, 1, 20, 22]
        self.assertEqual(actual_path, expected_path), "Incorrect DFS output with large graph"

    def test_get_bfs_path_when_target_is_end_node(self):
        graph_data.graph_data = [[
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2, 4]],
        [(200, 500), [3]]
        ]]
        global_game_data.target_node= [4]
        actual_path = pathing.get_bfs_path()
        expected_path = [1, 2, 3, 4]
        self.assertEqual(actual_path, expected_path), "Incorrect BFS output with target as last node"

    def test_get_dfs_path_when_target_is_end_node(self):
        graph_data.graph_data = [[
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2, 4]],
        [(200, 500), [3]]
        ]]
        global_game_data.target_node= [4]
        actual_path = pathing.get_dfs_path()
        expected_path = [1, 2, 3, 4]
        self.assertEqual(actual_path, expected_path), "Incorrect DFS output with target as last node"

    def test_calculate_total_distance_with_two_nodes(self):
        player_index = 0
        graph_data.graph_data = [[
        [(20, 20), [1]],
        [(50, 100), [0, 2]],
        ]]
        global_game_data.graph_paths = [[0, 1]]
        actual_distance = round(scoreboard.Scoreboard.calculate_total_distance(self, player_index), 10)
        expected_distance =  85.4400374532
        self.assertEqual(actual_distance, expected_distance), "Node distance not properly calculated with two nodes"

    def test_calculate_total_distance_with_multiple_nodes(self):
        player_index = 0
        graph_data.graph_data = [[
        [(0, 0), [1]],
        [(50, 200), [0, 2]],
        [(50, 300), [1, 3]],
        [(200, 500), [2, 4]],
        [(200, 500), [3]]
        ]]
        global_game_data.graph_paths = [[0, 1]]
        actual_distance = round(scoreboard.Scoreboard.calculate_total_distance(self, player_index), 10)
        expected_distance =  206.1552812809
        self.assertEqual(actual_distance, expected_distance), "Node distance not properly calculated with more than two nodes"

    def test_calculate_total_distance_with_negative_coordinates(self):
        player_index = 0
        graph_data.graph_data = [[
        [(0, 0), [1]],
        [(50, -10), [0, 2]],
        [(50, 30), [1, 3]],
        [(-20, 50), [2, 4]],
        [(20, -50), [3]]
        ]]
        global_game_data.graph_paths = [[0, 1]]
        actual_distance = round(scoreboard.Scoreboard.calculate_total_distance(self, player_index), 10)
        expected_distance =  50.9901951359
        self.assertEqual(actual_distance, expected_distance), "Node distance not properly calculated with negative coordinates"

    def test_calculate_distance_between_two_adjacent_nodes_with_start_node(self):
        player_index = 0
        graph_data.graph_data = [[
        [(20, 20), [1]],
        [(50, 100), [0, 2]],
        [(100, 300), [1]],
        ]]
        global_game_data.graph_paths = [[0, 1]]
        actual_distance = round(pathing.calculate_distance_between_two_adjacent_nodes(player_index, 0, 1), 10)
        expected_distance =  85.4400374532
        self.assertEqual(actual_distance, expected_distance), "Node distance not properly calculated with start node"

    def test_calculate_distance_between_two_adjacent_nodes_with_end_node(self):
        player_index = 0
        graph_data.graph_data = [[
        [(20, 20), [1]],
        [(50, 100), [0, 2]],
        [(100, 300), [1]],
        ]]
        global_game_data.graph_paths = [[0, 1]]
        actual_distance = round(pathing.calculate_distance_between_two_adjacent_nodes(player_index, 1, 2), 10)
        expected_distance =  206.1552812809
        self.assertEqual(actual_distance, expected_distance), "Node distance not properly calculated with end node"
    
    def test_calculate_distance_between_two_adjacent_nodes_with_small_distance(self):
        player_index = 0
        graph_data.graph_data = [[
        [(20, 20), [1]],
        [(1, 1), [0, 2]],
        [(1.0001, 1), [1, 3]],
        [(50, 100), [2]]
        ]]
        global_game_data.graph_paths = [[0, 1]]
        actual_distance = round(pathing.calculate_distance_between_two_adjacent_nodes(player_index, 1, 2), 10)
        expected_distance =  0.0001
        self.assertEqual(actual_distance, expected_distance), "Node distance not properly calculated with extremely small distance"

    def test_get_dijkstra_path_with_linear_path(self):
        graph_data.graph_data = [[
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2]]
        ]]
        global_game_data.target_node= [1]
        actual_path = pathing.get_dijkstra_path()
        expected_path = [1, 2, 3]
        self.assertEqual(actual_path, expected_path), "Incorrect dijkstra output with linear path"

    def test_dijkstra_with_cycle(self):
        graph_data.graph_data = [[
            [(0, 0), [1]],
            [(50, -200), [0, 2]],
            [(50, -300), [1, 3]],
            [(200, -500), [2, 0]]
        ]]
        global_game_data.target_node = [1]
        actual_path = pathing.get_dijkstra_path()
        expected_path = [1, 2, 3]
        self.assertEqual(actual_path, expected_path, "Incorrect dijkstra output with cyclical path")

    def test_dijkstra_with_multiple_branches(self):
        graph_data.graph_data = [[
            [(0, 0), [1, 2]],     
            [(50, -200), [0, 3, 4]],
            [(50, -300), [0, 5, 6]], 
            [(200, -400), [1]],   
            [(250, -400), [1, 7]],  
            [(300, -400), [2]],   
            [(350, -400), [2, 7]],   
            [(400, -500), [4, 6]]     
        ]]
        global_game_data.target_node = [3]  
        actual_path = pathing.get_dijkstra_path()
        expected_path = [1, 3, 1, 4, 7]
        self.assertEqual(actual_path, expected_path, "Dijkstra failed with a path containing multiple branches")

    def test_get_dijkstra_path_with_large_graph(self):
        graph_data.graph_data =  [[
            [(900, 0), [21, 22]],
            [(0, 300), [7, 19, 20]],
            [(100, 400), [9, 10, 20]],
            [(200, 0), [6, 8, 11, 22]],
            [(200, 200), [6, 7, 11, 12]],
            [(200, 500), [10, 21]],
            [(300, 100), [3, 4, 11, 20]],
            [(300, 300), [1, 4, 9, 12, 20]],
            [(400, 0), [3, 11, 22]],
            [(400, 300), [2, 7, 12, 13, 15]],
            [(400, 500), [2, 5, 13, 14, 15]],
            [(400, 100), [3, 4, 6, 8, 12, 16, 17]],
            [(400, 300), [4, 7, 9, 11, 15, 17]],
            [(400, 400), [9, 10, 15]],
            [(500, 500), [10, 18, 15]],
            [(600, 400), [9, 10, 12, 13, 14]],
            [(600, 0), [11, 17]],
            [(600, 200), [11, 12, 16, 18]],
            [(700, 400), [14, 17]],
            [(0, 500), [1, 8, 21]],
            [(0, 200), [1, 2, 6, 7, 22]],
            [(400, 700), [5, 19, 0]],
            [(0, 0), [0, 3, 20]]
        ]]
        global_game_data.target_node= [1]
        actual_path = pathing.get_dijkstra_path()
        expected_path = [22, 20, 1, 20, 22]
        self.assertEqual(actual_path, expected_path), "Incorrect dijkstra output with large graph"

    def test_get_dijkstra_path_when_target_is_end_node(self):
        graph_data.graph_data = [[
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2, 4]],
        [(200, 500), [3]]
        ]]
        global_game_data.target_node= [4]
        actual_path = pathing.get_dijkstra_path()
        expected_path = [1, 2, 3, 4]
        self.assertEqual(actual_path, expected_path), "Incorrect dijkstra output with target as last node"
    

    def test_get_dijkstra_path_with_equidistant_shortest_paths(self):
        graph_data.graph_data = [[
            [(0, 0), [1, 2]],
            [(50, -200), [0, 3]],
            [(50, -300), [0, 3]],
            [(100, -400), [1, 2]]
        ]]
        global_game_data.target_node= [3]
        actual_path = pathing.get_dijkstra_path()
        expected_paths = [[1, 2], [1,3]]
        self.assertIn(actual_path, expected_paths), "Incorrect dijkstra output with equidistant shortest paths"

if __name__ == '__main__':
    unittest.main()
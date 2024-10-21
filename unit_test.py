import math
import unittest
import pathing
import global_game_data
import graph_data
import scoreboard

class TestPathFinding(unittest.TestCase):

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
        self.assertEqual(actual_path, expected_path), "Incorrect BFS output with target as last node"

    # def test_calculate_total_distance_with_two_nodes(self):
    #     player_index = 0
    #     graph_data.graph_data = [[
    #     [(20, 20), [1]],
    #     [(50, 100), [0, 2]],
    #     ]]
    #     global_game_data.graph_paths = [[0, 1]]
    #     actual_distance = scoreboard.Scoreboard.calculate_total_distance(self, player_index)
    #     expected_distance =  85.440037453175
    #     self.assertEqual(actual_distance, expected_distance), "Node distance not properly calculated with two nodes"


if __name__ == '__main__':
    unittest.main()
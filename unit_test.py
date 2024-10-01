import math
import unittest
import pathing

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

    def test_valid_graph(self):
        graph = [
            [(0, 0), [1]],
            [(100, 100), [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertTrue(pathing.is_valid_graph(graph), "Should return True for a valid graph.")
    
    def test_graph_is_not_list(self):
        graph = (
            [(0, 0), [1]],
            [(100, 100), [0, 2]],
            [(200, 200), [1]]
        )
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when graph is not a list.")
    
    def test_node_data_is_not_list(self):
        graph = [
            ((0, 0), [1]),
            [(100, 100), [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when node_data is not a list.")
    
    def test_coordinates_are_not_tuple(self):
        graph = [
            ((0, 0), [1]),
            [[100, 100], [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when coordinates are not a tuple.")
    
    def test_adjacency_list_is_not_list(self):
        graph = [
            ((0, 0), 1),
            [(100, 100), [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when adjacency list is not a list.")
    
    def test_node_data_length_not_2(self):
        graph = [
            ((0, 0), 1),
            [(100, 100)],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when length of node_data is not 2.")

    def test_coordinates_length_not_2(self):
        graph = [
            [(0, 0), [1]],
            [(100, 100, 100), [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when length of coordinates is not 2.")
    
    def test_adjacency_list_not_filled_with_ints(self):
        graph = [
            [(0, 0), [1, 1.5]],
            [(100, 100), [0, 2]],
            [(200, 200), [1]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when adjacency list does not contain only integers.")

    def test_coordinates_not_numerical(self):
        graph = [
            [(0, 0), [1]],
            [(1, '1'), [0, 2]],
            [(0, 2), [1, 4]]
        ]
        self.assertFalse(pathing.is_valid_graph(graph), "Should return False when coordinates contain non-numerical value.")

if __name__ == '__main__':
    unittest.main()

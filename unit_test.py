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
        self.assertTrue(pathing.nodes_in_path_are_adjacent(path, graph), 'Returns False when graph is valid path.')

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
        self.assertFalse(pathing.nodes_in_path_are_adjacent(path, graph), 'Returns True when graph is invalid path.')

    def test_nodes_in_path_are_adjacent_with_single_node_path(self):
        graph =     [
        [(0, 0), [1]],
        [(1, 1), [0, 2]],
        [(0, 2), [1, 4]]
        ]
        path =  [1]
        pathing.nodes_in_path_are_adjacent(path, graph)
        self.assertTrue(pathing.nodes_in_path_are_adjacent(path, graph), 'Returns False with valid single node path.')

if __name__ == '__main__':
    unittest.main()

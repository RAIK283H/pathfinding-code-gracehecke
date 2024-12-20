'''
graph_data[a] = gives you graph at index a
graph_data[a][0] = start node of graph a
graph_data[a][length-1] = exit node of graph a
graph_data[a][b][0] = x-y coordinates as tuple of point b in graph a
graph_data[a][b][1] = adjacency list of point b in graph a

Only the start and exit nodes are dead ends (all other nodes have degree >= 2)
'''

sample_graph_data = [[
     # has hamiltonian cycles
        [(0, 0), [1, 9]],    
        [(1, 0), [0, 8, 2, 9]],
        [(2, 0), [1, 3]],    
        [(3, 0), [2, 4, 7]], 
        [(4, 0), [3, 5]],    
        [(5, 0), [4, 6]],    
        [(6, 0), [5, 7]],    
        [(7, 0), [3, 6, 8]], 
        [(8, 0), [1, 7, 9]],    
        [(9, 0), [0, 1, 8]]  
    ],
    # no cycles
    [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1]]
    ],
    # has hamiltonian cycles
   [
        [(0, 0), [1, 2, 4]],  
        [(1, 0), [0, 2, 3, 4]], 
        [(2, 0), [0, 1, 3]],  
        [(3, 0), [1, 2, 4]], 
        [(4, 0), [0, 1, 3]]   
    ]
]

graph_data = [

    [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1]]
    ],
    [
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2]]
    ],
    [
        [(900, 45), [17, 21, 22]],
        [(70, 350), [2, 7, 19, 20]],
        [(140, 420), [1, 5, 9, 10, 20]],
        [(210, 70), [6, 8, 11, 22]],
        [(210, 210), [6, 7, 11, 12, 20]],
        [(210, 490), [2, 10, 21]],
        [(280, 140), [3, 4, 11, 20]],
        [(280, 280), [1, 4, 9, 12, 20]],
        [(350, 70), [3, 11]],
        [(350, 350), [2, 7, 10, 12, 13, 15]],
        [(350, 490), [2, 5, 9, 13, 14, 15]],
        [(420, 140), [3, 4, 6, 8, 12, 16, 17]],
        [(420, 280), [4, 7, 9, 11, 15, 17]],
        [(420, 420), [9, 10, 15]],
        [(490, 490), [10, 18, 15]],
        [(560, 420), [9, 10, 12, 13, 14, 17, 18]],
        [(630, 70), [11, 17]],
        [(630, 210), [11, 12, 15, 16, 18, 0]],
        [(700, 420), [14, 15, 17, 23]],
        [(70, 500), [1, 21]],
        [(70, 210), [1, 2, 4, 6, 7, 22]],
        [(450, 700), [5, 19, 0, 23]],
        [(45, 45), [0, 3, 20]],
        [(1225, 700), [18, 21]]
    ],
    [
        [(0, 0), [1, 4]],
        [(0, 100), [0, 2, 5]],
        [(0, 200), [1, 3, 6]],
        [(0, 300), [2, 7]],
        [(100, 0), [5, 0, 8]],
        [(100, 100), [4, 6, 1, 9]],
        [(100, 200), [5, 7, 2, 10]],
        [(100, 300), [6, 3, 11]],
        [(200, 0), [9, 4, 12]],
        [(200, 100), [8, 10, 5, 13]],
        [(200, 200), [9, 11, 6, 14]],
        [(200, 300), [10, 7, 15]],
        [(300, 0), [13, 8]],
        [(300, 100), [12, 14, 9]],
        [(300, 200), [13, 15, 10]],
        [(300, 300), [14,11]],
    ],
    [
        [(45, 45), [1]],
        [(100, 245), [0, 2, 4]],
        [(200, 245), [1, 3, 5]],
        [(300, 145), [2, 6]],
        [(100, 345), [1, 5, 7]],
        [(200, 345), [2, 4, 6, 8]],
        [(300, 345), [3, 9]],
        [(100, 545), [4, 8]],
        [(200, 445), [5, 7, 9]],
        [(300, 445), [6, 8, 10]],
        [(1200, 700), [9]]
    ],
    [
        [(45, 45), [1]],
        [(100, 245), [14, 0, 2]],
        [(200, 245), [1, 5, 3]],
        [(300, 245), [2, 6, 10, 11, 12]],
        [(500, 345), [13, 6, 9]],
        [(200, 345), [14, 2, 6, 8]],
        [(300, 345), [9, 5, 4, 3]],
        [(100, 545), [8, 14]],
        [(200, 445), [5, 7, 9]],
        [(300, 445), [4, 6, 8, 15]],
        [(200, 145), [3, 11]],
        [(300, 145), [3, 10, 12]],
        [(400, 145), [3, 11, 13]],
        [(500, 145), [4, 12]],
        [(100, 345), [1, 7, 5]],
        [(1200, 700), [9]],
    ],
    [
        [(20, 20), [1]],
        [(30, 30), [0, 2]],
        [(40, 40), [1, 3]],
        [(50, 50), [2, 4]],
        [(60, 60), [3, 5]],
        [(70, 70), [4, 6]],
        [(80, 80), [5, 7]],
        [(90, 90), [6, 8]],
        [(100, 100), [7, 9]],
        [(110, 110), [8, 10]],
        [(120, 120), [9]]
    ],
        [
        [(120, 20), [1]],
        [(110, 30), [0, 2, 7]],
        [(100, 40), [1, 3]],
        [(90, 50), [2, 4, 8]],
        [(80, 60), [3, 5, 7]],
        [(70, 70), [4, 6]],
        [(80, 80), [5, 7]],
        [(90, 90), [1, 4, 6, 8]],
        [(100, 100), [7, 3, 9]],
        [(110, 110), [8, 10]],
        [(120, 120), [9]]
    ],
        [
        [(210, 90), [1]],
        [(100, 30), [0, 2, 7]],
        [(60, 50), [1, 3]],
        [(40, 150), [2, 4, 8, 11]],
        [(20, 10), [3, 5, 7, 11]],
        [(0, 0), [4, 6]],
        [(10, 200), [5, 7]],
        [(30, 100), [1, 4, 6, 8]],
        [(200, 60), [7, 3, 9]],
        [(70, 80), [8, 10]],
        [(90, 100), [9, 11]],
        [(210, 200), [3, 4, 10]]
    ],
        # extra credit
        [
        [(0, 0), [1, 25, 1, 5, 7, 15, 22, 25]],
        [(50, 0), [0, 2, 0, 2, 4, 7, 13, 18]],
        [(100, 0), [1, 3, 1, 3, 3, 3, 4, 10]],
        [(150, 0), [2, 4, 2, 2, 2, 4, 5, 6]],
        [(200, 0), [3, 5, 3, 1, 2, 5]],
        [(250, 0), [4, 6, 4, 0, 3, 6, 6, 9, 11, 13]],
        [(300, 100), [5, 7, 5, 3, 5, 7, 8, 12]],
        [(350, 100), [6, 8, 6, 0, 1, 8, 8, 14]],
        [(400, 100), [7, 9, 7, 7, 6, 9, 9, 11, 12, 14, 16, 17]],
        [(450, 100), [8, 10, 8, 8, 5, 10, 19]],
        [(500, 100), [9, 11, 9, 2, 11, 21, 25]],
        [(550, 200), [10, 12, 10, 8, 5, 12, 20]],
        [(600, 200), [11, 13, 11, 6, 8, 13]],
        [(650, 200), [12, 14, 12, 5, 1, 14]],
        [(700, 200), [13, 15, 13, 8, 7, 15, 19]],
        [(750, 200), [14, 16, 14, 0, 16, 22]],
        [(0, 300), [15, 17, 15, 8, 17, 20]],
        [(50, 300), [16, 18, 16, 8, 18]],
        [(100, 300), [17, 19, 17, 1, 19, 24]],
        [(150, 300), [18, 20, 18, 14, 9, 20, 23]],
        [(200, 300), [19, 21, 19, 11, 16, 21, 21]],
        [(250, 400), [20, 22, 20, 10, 20, 22]],
        [(300, 400), [21, 23, 21, 0, 15, 23]],
        [(350, 400), [22, 24, 22, 19, 24]],
        [(400, 400), [23, 25, 23, 18, 25]],
        [(450, 400), [0, 24, 0, 24, 10]]
    ]
]

test_path = [
    [1, 2],
    [1, 2, 3],
    [22, 3, 11, 17, 18, 23],
    [1, 5, 6, 10, 11, 15],
    [1, 2, 5, 8, 9, 10],
    [1, 14, 5, 6, 9, 15],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 7, 8, 9, 10],
    [1, 2, 3, 11],
    # extra credit
    [0, 25]
]

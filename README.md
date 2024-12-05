# Pathfinding Starter Code

The get_random_path function finds a list of adjacent nodes of the curr_node (beginning with start node 0). A node is randomly selected from this adjacency list, set to curr_node, and appended to a list of nodes that stores the path. If the appended node is the target node, target_hit is set to True. A while loop continues the above steps with the new curr_node until the target has been hit (target_hit = True), and the curr_node is the exit_node. The function returns the path with all of the appended nodes.

The added statistic represents the number of times a node is visited during a player's graph traversal, after the start node. When a player reaches a node, the value is incremented. If the same node is hit repeatedly, the value is still incremented on each pass through.

FLOYD-WARSHALL EC:

The former BFS player now displays a Floyd-Warshall player with the appropriate path.

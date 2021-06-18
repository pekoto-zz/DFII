import queue as queue_lib
from collections import deque
from typing import List, Set, Deque

from data_structures.directed_graph_unweighted import DirectedGraphUnweighted


class BFS:
    """A breadth-first search (BFS) graph traversal implementation.

    If you think of the graph like a tree, then a BFS will visit all of the nodes
    on the same level first.

    1. Declare edge_to, distance_to dicts
    2. Declare visited set
    3. While the queue is not empty:
        3.1 Dequeue the next vertex
        3.2 For each neighbour...
        3.3 If the neighbour not visited, update edge_to and distance to, and
            add it to the queue.
        3.4 Repeat for next element in the queue.

    Usages after construction:
    1. Find it two nodes are connected O(1)
    2. Get the path to another node O(length of path)
    3. Get the path length/shortest path to another node O(1)
        (Since vertices are processed in order, BFS will return shortest path.)

    Performance:
        Initial construction: O(V+E) -- number of vertices + edges
        Space: O(V) -- edge_to and distance_to lists

    Uses:
     - Quickly get distance to any other node
     - Number of leaps in a network
     - Degrees of separation
    """

    def __init__(self, graph: DirectedGraphUnweighted, starting_vertex: str) -> None:
        """Initializes the BFS class."""
        self._starting_vertex = starting_vertex
        self._edge_to = {}
        self._distance_to = {}
        self._visited = set()

        for vertex in graph.vertices():
            self._distance_to[vertex] = 0

        self._bfs(graph, starting_vertex)

    def _bfs(self, graph: DirectedGraphUnweighted, starting_vertex: str) -> None:
        """Performs the BFS.

        1. Declare a queue and put on the starting vertex.
        2. While the queue is not empty...
        2.1 Get the vertex
        2.2 Set distance to be distance to this vertex + 1
        2.3 For each neighbour...
        3. If it hasn't been visited...
        3.1 Set edge_to this neighbour to be the vertex
        3.2 Set distance to this neighbour to be the distance
        3.3 Put the neighbour on the queue
        3.4 Mark the neighbour visited

        :param graph: The graph to BFS.
        :param starting_vertex: The starting vertex.
        """
        queue = queue_lib.Queue()
        queue.put(starting_vertex)

        while not queue.empty():
            vertex = queue.get()
            distance = self._distance_to[vertex] + 1

            for neighbour in graph.neighbours_to(vertex):
                if neighbour not in self._visited:
                    self._edge_to[neighbour] = vertex
                    self._distance_to[neighbour] = distance
                    queue.put(neighbour)
                    self._visited.add(neighbour)

    def path_exists(self, vertex: str) -> bool:
        """Checks if a path exists in the visited nodes."""
        return vertex in self._visited

    def path_to(self, destination_vertex: str) -> List[str]:
        """Finds a path to the destination vertex, or raises an Exception if no path exists.

        1. Set up a deque (stack)
        2. Get the edge to this vertex
        3. While we haven't reached the starting vertex...
        4. Add the edge to this vertex to the path
        5. Set the next vertex the edge to that vertex.

        :param destination_vertex: The vertex you want to find a path to.
        :return: List of nodes leading to the destination vertex.
        """
        if not self.path_exists(destination_vertex):
            raise Exception("No path exists!")

        path = deque()
        path.append(destination_vertex)

        vertex = self._edge_to[destination_vertex]

        while vertex != self._starting_vertex:
            path.appendleft(vertex)
            vertex = self._edge_to[vertex]

        path.appendleft(self._starting_vertex)

        return list(path)

    def distance_to(self, destination_vertex: str) -> int:
        """Returns the distance to the destination vertex."""
        if not self.path_exists(destination_vertex):
            raise Exception("No path exists!")

        return self._distance_to[destination_vertex]

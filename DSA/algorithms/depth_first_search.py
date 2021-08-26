from collections import deque
from typing import List

from data_structures.directed_graph_unweighted import DirectedGraphUnweighted


class DFS:
    """A Depth-First Search (DFS) graph traversal implementation.

    If you think of the graph like a tree, DFS will traverse all the way down to the
    root of one branch, before doing to the next.

    1. Declare edge_to and visited dictionaries
    2. Mark the current vertex as visited
    3. For each of the neighbours...
    3.1 If the neighbour has been visited, dfs to that neighbour recursively
    3.2 Set the edge to this neighbour to be the initial vertex.

    Usages after construction:
    * Find if the starting vertex is connected O(1)
    * Get the path to another node O(length of path)

    Performance:
    * Construction: O(V+E) -- vertices + edges
    * Space: O(V)

    Uses:
    * Detect a cycle in a graph
    * Path finding
    * Topological sorting
    * Find strongly connected components
    """

    def __init__(self, graph: DirectedGraphUnweighted, starting_vertex: str) -> None:
        """Initializes the DFS class."""
        self._starting_vertex = starting_vertex
        self._edge_to = {}
        self._visited = set()

        self._dfs(graph, starting_vertex)

    def _dfs(self, graph: DirectedGraphUnweighted, vertex: str) -> None:
        """Runs the main DFS algorithm.

        1. Mark the vertex as visited
        2. For each neighbour that hasn't been visited...
        3. DFS that neighbour
        4. Set the edge_to to that neighbour to the vertex.

        :param graph: The graph to DFS.
        :param vertex: The current vertex.
        """
        self._visited.add(vertex)

        for neighbour in graph.neighbours_to(vertex):
            if neighbour not in self._visited:
                self._dfs(graph, neighbour)
                self._edge_to[neighbour] = vertex

    def path_exists(self, destination_vertex: str) -> bool:
        """Returns True if a path exists from the starting vertex to the destination vertex."""
        return destination_vertex in self._visited

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
            raise Exception("Path does not exist!")

        path = deque()
        path.append(destination_vertex)

        vertex = self._edge_to[destination_vertex]

        while vertex != self._starting_vertex:
            path.appendleft(vertex)
            vertex = self._edge_to[vertex]

        path.appendleft(vertex)

        return list(path)

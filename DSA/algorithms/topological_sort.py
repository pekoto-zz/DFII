from typing import List, Set

from data_structures.directed_graph_unweighted import DirectedGraphUnweighted


def topological_sort(graph: DirectedGraphUnweighted) -> List[str]:
    """Returns a topological sorting of a graph, or raises an Exception if a loop is found.

    1. Declare visited and ordering structures.
    2. For every vertex...
        2.1 If it hasn't been visited, kick off a depth first search
        2.2 Add the vertex to visited and recursion stack
        2.3 For each neighbour...
            2.3.1 If it's in the recursion stack, there's a loop
            2.3.2 If it hasn't been visited, dfs the neighbour
        2.4 Add the vertex to the ordering
        2.5 Remove it from the recursion stack.
    3. Return the ordering in reverse.

    Time: O(v+e): We traverse every vertex and edge.
    Space: O(v): Need to store every vertex.

    :param graph: The graph to topologically order.
    :return: A topological ordering of the nodes.
    """
    visited = set()
    ordering = []

    for vertex in graph.vertices():
        if vertex not in visited:
            _dfs(graph, vertex, visited, ordering)

    # Returns the ordering in reverse.
    return ordering[::-1]


def _dfs(graph: DirectedGraphUnweighted,
         vertex: str,
         visited: Set[str],
         ordering: List[str],
         stack: Set[str] = None) -> None:
    """Performs a depth first search on a vertex, and detects loops.

    :param graph: The graph to search.
    :param vertex: The vertex to search from.
    :param visited: Whether the vertex has been visited.
    :param ordering: The ordering of the vertices.
    :param stack: The recursion stack, for detecting loops.
    """
    stack = stack if stack else set()

    visited.add(vertex)
    stack.add(vertex)

    for neighbour in graph.neighbours_to(vertex):
        if neighbour in stack:
            raise Exception(f'Cycle found in graph: {vertex}<>{neighbour}')

        if neighbour not in visited:
            _dfs(graph, neighbour, visited, ordering, stack)

    ordering.append(vertex)
    stack.remove(vertex)

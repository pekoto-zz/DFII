class DirectedGraphUnweighted:
    """A directed graph implementation using adjacency list.

    (Actually we can use a set instead of a list to make things faster.)

    To turn it into an undirected graph, we would just connect b to a in the connect method.

    Operations:
        add_vertex: O(1) average, O(n) worst case
        connect: O(1) average, O(n) worst case
        is_connected: O(1) average, O(n) worst case

    Space:
        O(V+E) = vertices + edges
    """

    def __init__(self):
        """Initializes the directed graph."""
        self._vertices = {}

    def add_vertex(self, vertex_id: str) -> None:
        """Adds or reinitializes a vertex in the graph.

        Time: O(1) average, O(n) worst case

        :param vertex_id: The id of the vertex to add.
        :return: None.
        """
        self._vertices[vertex_id] = set()

    def connect(self, vertex_a: str, vertex_b: str) -> None:
        """Connects vertex a to vertex b, or raises KeyError if vertex not found.

        Time: O(1) average, O(n) worst case

        :param vertex_a: The vertex to connect.
        :param vertex_b: The vertex to connect to.
        :return: None.
        """
        if vertex_a not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_a}')

        if vertex_b not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_b}')

        self._vertices[vertex_a].add(vertex_b)
        # To create an undirected graph, we just connect b to a too.

    def is_connected(self, vertex_a: str, vertex_b: str) -> bool:
        """Returns True if vertex a is connected to vertex b directionally.

        Time: O(1) average, O(n) worst case

        :param vertex_a: The starting vertex.
        :param vertex_b: The vertex connected to.
        :return: True if vertex a is connected to vertex b, False otherwise.
        """
        if vertex_a not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_a}')

        if vertex_b not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_b}')

        return vertex_b in self._vertices[vertex_a]

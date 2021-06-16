import unittest

from data_structures.directed_graph_unweighted import DirectedGraphUnweighted


class DirectedGraphUnweightedTest(unittest.TestCase):

    def test_graph(self):
        """Basically we need to test all methods together.

        The graph should look like this:

        a---->b
        |     |
        v     v
        c---->d---->e
        """
        graph = DirectedGraphUnweighted()

        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")

        graph.connect("a", "b")
        graph.connect("a", "c")
        graph.connect("b", "d")
        graph.connect("c", "d")
        graph.connect("d", "e")

        self.assertTrue(graph.is_connected("a", "b"))
        self.assertTrue(graph.is_connected("a", "c"))
        self.assertTrue(graph.is_connected("b", "d"))
        self.assertTrue(graph.is_connected("c", "d"))
        self.assertTrue(graph.is_connected("d", "e"))

        self.assertFalse(graph.is_connected("a", "e"))
        self.assertFalse(graph.is_connected("a", "d"))
        self.assertFalse(graph.is_connected("b", "c"))
        self.assertFalse(graph.is_connected("b", "e"))
        self.assertFalse(graph.is_connected("c", "e"))

    def test_connect_throws_error_if_vertex_not_found(self):
        graph = DirectedGraphUnweighted()

        with self.assertRaises(KeyError):
            graph.connect("a", "b")

    def test_is_connected_throws_error_if_vertex_not_found(self):
        graph = DirectedGraphUnweighted()

        with self.assertRaises(KeyError):
            graph.is_connected("a", "b")

    def test_neighbours(self):
        """
         a---->b
        |     |
        v     v
        c---->d---->e
        """
        graph = DirectedGraphUnweighted()

        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")

        graph.connect("a", "b")
        graph.connect("a", "c")
        graph.connect("b", "d")
        graph.connect("c", "d")
        graph.connect("d", "e")

        self.assertSetEqual(set(["b", "c"]), graph.neighbours_to("a"))
        self.assertSetEqual(set(["d"]), graph.neighbours_to("b"))
        self.assertSetEqual(set(["d"]), graph.neighbours_to("c"))
        self.assertSetEqual(set(["e"]), graph.neighbours_to("d"))

    def test_vertices(self):
        """
         a---->b
        |     |
        v     v
        c---->d---->e
        """
        graph = DirectedGraphUnweighted()

        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")

        self.assertListEqual(["a", "b", "c", "d", "e"], graph.vertices())


if __name__ == '__main__':
    unittest.main()

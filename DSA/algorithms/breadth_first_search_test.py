import unittest

from algorithms.breadth_first_search import BFS
from data_structures.directed_graph_unweighted import DirectedGraphUnweighted


class BreadthFirstSearchTest(unittest.TestCase):

    def test_path_exists(self):
        """
        The graph should look like this:

        a---->b<----f
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
        graph.add_vertex("f")

        graph.connect("a", "b")
        graph.connect("a", "c")
        graph.connect("b", "d")
        graph.connect("c", "d")
        graph.connect("d", "e")
        graph.connect("f", "b")

        bfs = BFS(graph, "a")

        self.assertTrue(bfs.path_exists("b"))
        self.assertTrue(bfs.path_exists("c"))
        self.assertTrue(bfs.path_exists("d"))
        self.assertTrue(bfs.path_exists("e"))
        self.assertFalse(bfs.path_exists("f"))

    def test_distance_to(self):
        """
        The graph should look like this:

        a---->b<----f
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
        graph.add_vertex("f")

        graph.connect("a", "b")
        graph.connect("a", "c")
        graph.connect("b", "d")
        graph.connect("c", "d")
        graph.connect("d", "e")
        graph.connect("f", "b")

        bfs = BFS(graph, "a")

        self.assertEqual(1, bfs.distance_to("b"))
        self.assertEqual(1, bfs.distance_to("c"))
        self.assertEqual(2, bfs.distance_to("d"))
        self.assertEqual(3, bfs.distance_to("e"))

    def test_path_to(self):
        """
        The graph should look like this:

        a---->b<----f
        |     |
        v     v
        c     d---->e
        """
        graph = DirectedGraphUnweighted()

        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")
        graph.add_vertex("f")

        graph.connect("a", "b")
        graph.connect("a", "c")
        graph.connect("b", "d")
        graph.connect("d", "e")
        graph.connect("f", "b")

        bfs = BFS(graph, "a")

        self.assertListEqual(["a", "b"], bfs.path_to("b"))
        self.assertListEqual(["a", "c"], bfs.path_to("c"))
        self.assertTrue(["a", "b", "d"], bfs.path_to("d"))
        self.assertTrue(["a", "b", "d", "e"], bfs.path_to("e"))


if __name__ == '__main__':
    unittest.main()

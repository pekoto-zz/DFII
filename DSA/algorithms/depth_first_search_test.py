import unittest

from algorithms.depth_first_search import DFS
from data_structures.directed_graph_unweighted import DirectedGraphUnweighted


class DepthFirstSearchTest(unittest.TestCase):

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

        dfs = DFS(graph, "a")

        self.assertTrue(dfs.path_exists("b"))
        self.assertTrue(dfs.path_exists("c"))
        self.assertTrue(dfs.path_exists("d"))
        self.assertTrue(dfs.path_exists("e"))
        self.assertFalse(dfs.path_exists("f"))

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

        dfs = DFS(graph, "a")

        self.assertListEqual(["a", "b"], dfs.path_to("b"))
        self.assertListEqual(["a", "c"], dfs.path_to("c"))
        self.assertListEqual(["a", "b", "d"], dfs.path_to("d"))
        self.assertListEqual(["a", "b", "d", "e"], dfs.path_to("e"))


if __name__ == '__main__':
    unittest.main()

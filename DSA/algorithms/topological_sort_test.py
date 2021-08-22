import unittest

from algorithms.topological_sort import topological_sort
from data_structures.directed_graph_unweighted import DirectedGraphUnweighted


class TopologicalSortTest(unittest.TestCase):

    def test_topological_sort(self):
        """
        5-->0<--4
        |       |
        ˇ       ˇ
        2-->3-->1
        """
        graph = DirectedGraphUnweighted()
        graph.add_vertex('0')
        graph.add_vertex('1')
        graph.add_vertex('2')
        graph.add_vertex('3')
        graph.add_vertex('4')
        graph.add_vertex('5')

        graph.connect('2', '3')
        graph.connect('3', '1')
        graph.connect('4', '0')
        graph.connect('4', '1')
        graph.connect('5', '0')
        graph.connect('5', '2')

        topological_sorting = topological_sort(graph)

        self.assertListEqual(['5', '4', '2', '3', '1', '0'], topological_sorting)  # add assertion here

    def test_topological_sort_raises_exception_when_graph_contains_cycle(self):
        """
        5-->0<--4
        |       |
        ˇ       ˇ
        2-->3<->1
        """
        graph = DirectedGraphUnweighted()
        graph.add_vertex('0')
        graph.add_vertex('1')
        graph.add_vertex('2')
        graph.add_vertex('3')
        graph.add_vertex('4')
        graph.add_vertex('5')

        graph.connect('2', '3')
        graph.connect('3', '1')
        graph.connect('1', '3')  # Cycle
        graph.connect('4', '0')
        graph.connect('4', '1')
        graph.connect('5', '0')
        graph.connect('5', '2')

        with self.assertRaises(Exception):
            _ = topological_sort(graph)


if __name__ == '__main__':
    unittest.main()

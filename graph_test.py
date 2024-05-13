"""Tests for graphs."""

import unittest

import graph as m


class GraphsTestCase(unittest.TestCase):
    """Tests."""

    def testDfs(self):
        dfs = m.Dfs()
        # That's actually not correct for the undirected graph, we need
        # the back edge, i.e. (2, 0)
        dfs.add_edge(0, 2)
        dfs.add_edge(0, 5)
        dfs.add_edge(0, 1)
        dfs.add_edge(1, 2)
        dfs.add_edge(5, 3)
        dfs.add_edge(3, 2)
        dfs.add_edge(2, 4)
        dfs.add_edge(3, 4)

        dfs.run_dfs(0)

    def testBfs(self):
        bfs = m.Bfs()
        bfs.add_edge(0, 2)
        bfs.add_edge(0, 5)
        bfs.add_edge(0, 1)
        bfs.add_edge(1, 2)
        bfs.add_edge(5, 3)
        bfs.add_edge(3, 2)
        bfs.add_edge(2, 4)
        bfs.add_edge(3, 4)
        bfs.add_edge(9, 10)

        bfs.run_bfs(0)
        print(bfs.path_to(4))
        self.assertTrue(bfs.has_path_to(4))
        self.assertFalse(bfs.has_path_to(10))

    def testBfsEx(self):
        """
        0
        2, 5, 1
        4  3

        9
        10
        """
        s = m.GraphNode(0)
        one = m.GraphNode(1)
        two = m.GraphNode(2)
        three = m.GraphNode(3)
        four = m.GraphNode(4)
        five = m.GraphNode(5)
        bfs = m.BfsEx()
        bfs.add_edge(s, two)
        bfs.add_edge(s, five)
        bfs.add_edge(s, one)
        bfs.add_edge(one, two)
        bfs.add_edge(five, three)
        bfs.add_edge(three, two)
        bfs.add_edge(two, four)
        bfs.add_edge(three, four)
        bfs.add_edge(m.GraphNode(9), m.GraphNode(10))

        bfs.run(s)


if __name__ == "__main__":
    unittest.main()

"""Graphs basics."""

import collections


class Dfs:
    """Run DFS."""

    def __init__(self):
        self.graph = collections.defaultdict(set)
        self.marked = set()

    def add_edge(self, v1, v2):
        self.graph[v1].add(v2)
        self.graph[v2].add(v1)

    def visit_all(self):
        self.marked.clear()
        self.run_dfs(self.graph[0])

    def run_dfs(self, v):
        print(v)
        self.marked.add(v)

        # This 'for' loop if there's adjacency list. In cases of matrices or
        # strings or trees, it should be some kind of for-loop.
        for w in self.graph[v]:
            if w not in self.marked:
                self.run_dfs(w)


class Bfs:
    """Run BFS."""

    def __init__(self):
        self.graph = collections.defaultdict(set)
        self.marked = set()
        # edge[2] = 0 means we came to '2' from '0'
        self.edge_to = collections.defaultdict(int)
        self.s = None

    def add_edge(self, v1, v2):
        self.graph[v1].add(v2)
        self.graph[v2].add(v1)

    def run_bfs(self, s):
        self.s = s
        self.marked.clear()
        self.edge_to.clear()
        queue = collections.deque()
        self.marked.add(s)
        queue.append(s)
        while queue:
            v = queue.popleft()
            print(v)
            for w in self.graph[v]:
                if w not in self.marked:
                    self.edge_to[w] = v
                    self.marked.add(w)
                    queue.append(w)

    def has_path_to(self, v):
        return v in self.marked

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        x = v
        path = []
        while x != self.s:
            x = self.edge_to[x]
            path.append(x)
        path.append(self.s)
        return path


# Vertex coloring:
# WHITE - undiscovered
# GRAY - discovered, but not yet explored, that is on the frontier
# BLACK - discovered and explored
WHITE, GRAY, BLACK = range(3)


class GraphNode:
    """Three-color graph node with some other attributes."""

    def __init__(self, data=None, parent=None, level=0):
        self.data = data
        self.color = WHITE
        self.parent = parent
        self.level = level

    def __repr__(self):
        return f"data:{self.data} color:{self.color} parent:{self.parent.data
            if self.parent else "None"} level:{self.level}"


class BfsEx:
    """Three-color version.
     Has no marked set because vertex is an object which has
    color attribute. Color serves the purpose of both marked
    indicator and also additional info that can be used during
    some other analysis, like cycle detection.

    """

    def __init__(self):
        self.graph = collections.defaultdict(set)
        self.s = None

    def add_edge(self, v1, v2):
        self.graph[v1].add(v2)
        self.graph[v2].add(v1)

    def run(self, s):
        self.s = s
        s.color = GRAY
        queue = collections.deque()
        queue.append(s)
        while queue:
            v = queue.popleft()
            print(f"v:{v.data}")
            for w in self.graph[v]:
                if w.color == WHITE:
                    w.color = GRAY  # Not yet explored, on the edge
                    w.level = v.level + 1
                    w.parent = v
                    print(f"Adding w - {w}")
                    queue.append(w)
                v.color = BLACK  # Done with this vertex

        print("Done")

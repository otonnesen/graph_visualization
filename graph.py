class Graph:
    def __init__(self):
        self._n = 0
        self._e = 0
        self._edge_labels = {}
        self._adj_list = {}

    def add_edge(self, u, v):
        if self.has_edge(u, v):
            return None
        if not self.has_vertex(u) or not self.has_vertex(v):
            return None

        self._e += 1
        self._adj_list[u].append(v)
        self._adj_list[v].append(u)
        return repr(u)+','+repr(v)

    def add_vertex(self, l=None):
        if self.has_vertex(l):
            return None
        if l is None:
            l = self._n
        self._n += 1
        self._adj_list[l] = []
        return l

    def degree(self, v):
        return len(self._adj_list[v])

    def del_edge(self, u, v):
        if not self.has_edge(u, v):
            return
        self._adj_list[u].remove(v)
        self._adj_list[v].remove(u)

    def del_vertex(self, v):
        if not self.has_vertex(v):
            return
        del self._adj_list[v]
        for u in self._adj_list:
            if v in self._adj_list[u]:
                self._adj_list[u].remove(v)

    def has_edge(self, u, v):
        return u in self._adj_list[v] and v in self._adj_list[u]

    def has_vertex(self, v):
        return v in self._adj_list.keys()

    def iterator_edges(self, v):
        pass

    def iterator_neighbors(self, v):
        pass

    def num_edges(self):
        return self._e

    def num_vertices(self):
        return self._n

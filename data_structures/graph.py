class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

        self.discovery = 0
        self.finish = 0
        self.status = 'undiscovered'
        self.distance = 9999

    def add_neighbors(self, v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbors(v)
                if key == v:
                    value.add_neighbors(u)
            return True
        else:
            return False

    def print_graph(self):
        amount_neighbors = []
        for key in sorted(list(self.vertices.keys())):
            amount_neighbors.append(len(self.vertices[key].neighbors))
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors).ljust(1+5*max(amount_neighbors)) + str(self.vertices[key].discovery) + "/" + str(self.vertices[key].finish) + " Distance: " + str(self.vertices[key].distance))

    def _dfs(self, vertex):
        global time
        vertex.status = 'discovered'
        vertex.discovery = time
        time += 1
        for v in vertex.neighbors:
            if self.vertices[v].status == 'undiscovered':
                self._dfs(self.vertices[v])
        vertex.status = 'finished'
        vertex.finish = time
        time += 1

    def dfs(self, start):
        global time
        time = 1
        self._dfs(start)

    def bfs(self, vertex):
        queue = list()
        vertex.distance = 0
        vertex.status = 'visited'
        for v in vertex.neighbors:
            self.vertices[v].distance = vertex.distance + 1
            queue.append(v)

        while len(queue) > 0:
            current = self.vertices[queue.pop(0)]
            current.status = 'visited'
            for v in current.neighbors:
                next = self.vertices[v]
                if next.status == 'undiscovered':
                    queue.append(v)
                    if next.distance > current.distance + 1:
                        next.distance = current.distance + 1




g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])
m = Vertex('M')
g.add_vertex(m)
g.add_edge('C', 'M')
g.add_edge('F', 'M')

g.dfs(a)
#g.bfs(m)
g.print_graph()

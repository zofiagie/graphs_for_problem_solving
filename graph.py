class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}      # list of neighbors with weights

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' -> ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, vert):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(vert)
        self.vert_list[vert] = new_vertex
        return new_vertex

    def add_edge(self, from_vert, to_vert, weight=0):
        if from_vert not in self.vert_list:
            nv = self.add_vertex(from_vert)
        if to_vert not in self.vert_list:
            nv = self.add_vertex(to_vert)
        self.vert_list[from_vert].add_neighbor(self.vert_list[to_vert], weight)

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def get_vertices(self):
        return self.vert_list.keys()

    def get_edges(self):
        for i in self.vert_list:
            if len(self.vert_list[i].connected_to.keys()) != 0:
                print(self.vert_list[i])

    def __contains__(self, n):
        return n in self.vert_list

    def bfs(self, start):
        visited = {}    # dictionary of visited vertices
        for i in self.vert_list:
            visited[self.vert_list[i].id] = False
        queue = [start]
        visited[start] = True
        while queue:
            temp = queue.pop(0)
            print(temp, end=" ")
            for i in self.get_vertex(temp).connectedTo:
                if not visited[i.id]:
                    queue.append(i.id)
                    visited[i.id] = True

    def dfs_util(self, v, visited, stack):
        visited[v] = True
        stack.append(v)
        for i in self.get_vertex(v).connectedTo:     # recursion over all vertices adjacent to v
            if not visited[i.id]:
                self.dfs_util(i.id, visited, stack)

    def dfs(self, start):
        stack = []
        visited = {}
        for i in self.vert_list:
            visited[self.vert_list[i].id] = False
        self.dfs_util(start, visited, stack)
        return stack

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.get_vertex(v).connectedTo:
            if not visited[i.id]:
                self.topological_sort_util(i.id, visited, stack)
        stack.insert(0, v)       # adding to the stack those vertices for which all adjacent vertices have been visited

    def topological_sort(self):
        visited = {}
        for i in self.vert_list:
            visited[self.vert_list[i].id] = False
        stack = []
        for i in self.vert_list.keys():
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        return stack


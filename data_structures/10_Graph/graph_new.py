class Graph:
    def __init__(self):
        # Creates an empty adjacency list self.adj_list to store the graph's vertices and edges.
        self.adj_list = {}

    def print_graph(self):
        # Collects all the vertices into a list.
        # Sorts the list to ensure vertices are printed in alphabetical (or numerical) order.
        # For each vertex, prints the vertex and its list of adjacent vertices.
        v_list = []
        for vertex in self.adj_list:
            v_list.append(vertex)
        v_list.sort()
        for v in v_list:
            print(v, ':', self.adj_list[v])

    def add_vertex(self, vertex):
        # If the vertex is not already in the adjacency list, it is added with an empty list as its value.
        # Returns True if the vertex was added, False otherwise (e.g., if the vertex already exists).
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        # First checks if both v1 and v2 exist in the graph.
        # Adds v2 to the adjacency list of v1 and v1 to the adjacency list of v2, representing an undirected edge.
        # Returns True if the edge was added, False otherwise.
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        # Checks if both v1 and v2 exist in the graph.
        # Tries to remove v2 from the adjacency list of v1 and v1 from the adjacency list of v2.
        # Handles ValueError in case an edge does not exist.
        # Returns True if the operation is successful, False otherwise.
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): 
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self,vertex):
        # Checks if the vertex exists in the graph.
        # Removes the vertex from the adjacency lists of all other vertices it is connected to.
        # Deletes the vertex from the graph.
        # Returns True if the operation is successful, False otherwise.
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False




my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')


print('Graph before remove_vertex():')
my_graph.print_graph()


my_graph.remove_vertex('D')


print('\nGraph after remove_vertex():')
my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    Graph before remove_vertex():
    A : ['B', 'C', 'D']
    B : ['A', 'D']
    C : ['A', 'D']
    D : ['A', 'B', 'C']

    Graph after remove_vertex():
    A : ['B', 'C']
    B : ['A']
    C : ['A']

"""
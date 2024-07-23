class Graph:
    def __init__(self):
        self.adjList = {}  # to save adjacency list
        self.edges = []  # to save all edges

class Edge:
    def __init__(self, u, v, distance):
        self.u = u
        self.v = v
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item): #O(log V)
        if self.parent[item] == item: 
            return item
        else:
            self.parent[item] = self.find(self.parent[item]) 
            return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1) #O(log V)
        root2 = self.find(set2) #O(log V)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]: 
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def Kruskal(graph):
    graph.edges.sort() #@O(E log E)
    
    disjoint_set = DisjointSet(graph.adjList.keys()) #O(V)
    mst = []  
    
    for edge in graph.edges: #(E)
        u, v = edge.u, edge.v
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v) #O(E log V)
            mst.append(edge)

    return mst

def read_graph_from_file(filename):
    graph = Graph()
    
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        
    reading_connections = False
    for line in lines:
        if line.startswith("Connections and Distances:"):
            reading_connections = True
            continue
        
        if reading_connections:
            if not line.strip():
                continue
            star, connections = line.split(":")
            star = star.strip()
            graph.adjList[star] = []
            connections = connections.split(", ")
            for conn in connections:
                conn_star, distance = conn.split(" (")
                conn_star = conn_star.strip()
                distance = float(distance.strip()[:-1])
                edge = Edge(star, conn_star, distance)
                graph.adjList[star].append(edge)
                if star < conn_star:  
                    graph.edges.append(edge)
    
    return graph

if __name__ == "__main__":
    
    graph = read_graph_from_file('dataset2.txt')
    
    result_lines = []
    for vertex, edges in graph.adjList.items():
        edge_strs = [f"({edge.v}, {edge.distance})" for edge in edges]
        result_lines.append(f"{vertex}: {', '.join(edge_strs)}")

    
    mst = Kruskal(graph)
 
    result_lines.append("\nMinimum Spanning Tree:")
    for edge in mst:
        result_lines.append(f"({edge.u}, {edge.v}, {edge.distance})")

    
    with open('Kruskal_results.txt', 'w') as outfile:
        for line in result_lines:
            outfile.write(line + "\n")
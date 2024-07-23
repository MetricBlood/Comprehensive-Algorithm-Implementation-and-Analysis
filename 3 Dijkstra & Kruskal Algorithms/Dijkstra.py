from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.adjList = {}  # to save adjacency list #(V + E) space

class Edge:
    def __init__(self, distance, vertex):
        self.distance = distance
        self.vertex = vertex

def Dijkstra(graph , start):
    previous = {v: None for v in graph.adjList.keys()} 
    visited = {v: False for v in graph.adjList.keys()}
    distance = {v: float('inf') for v in graph.adjList.keys()}
    distance[start] = 0
    queue = PriorityQueue()
    queue.put((0, start)) #O(log n)
    
    while not queue.empty(): # O(V)
        removed_distance, removed_vertex = queue.get()  # will return the distance and the removed element.  O(log n)
        
        if visited[removed_vertex]:
            continue

        visited[removed_vertex] = True
        
        for edge in graph.adjList[removed_vertex]: # O(V + E)
            if visited[edge.vertex]:
                continue
            new_distance = removed_distance + edge.distance
            if new_distance < distance[edge.vertex]:
                distance[edge.vertex] = new_distance
                previous[edge.vertex] = removed_vertex
                queue.put((new_distance, edge.vertex))
    
    return distance, previous

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
            
            # Split the line by ":"
            star, connections = line.split(":")
            star = star.strip()  # Remove leading/trailing whitespace
            graph.adjList[star] = []
            
            
            connections = connections.split(", ")
            for conn in connections:
                
                conn_star, distance = conn.split(" (")
                conn_star = conn_star.strip()  # Remove leading/trailing whitespace
                distance = float(distance[:-2])  # Remove trailing ')' and convert to float
                
                # Create Edge object and add to adjacency list
                graph.adjList[star].append(Edge(distance, conn_star))
    
    return graph

if __name__ == "__main__":
    graph = read_graph_from_file('dataset2.txt')
    
    for vertex, edges in graph.adjList.items():
        edge_strs = [f"({edge.vertex}, {edge.distance})" for edge in edges]
        print(f"{vertex}: {', '.join(edge_strs)}")

if __name__ == "__main__":
    
    graph = read_graph_from_file('dataset2.txt')
    
    
    result_lines = []

    # just some formaitng 
    for vertex, edges in graph.adjList.items():
        edge_strs = [f"({edge.vertex}, {edge.distance})" for edge in edges]
        result_lines.append(f"{vertex}: {', '.join(edge_strs)}")

    # Run Dijkstra
    start_vertex = 'A'  
    distances, previous_nodes = Dijkstra(graph, start_vertex)
    print("Distances from start vertex:", distances)
    print("Previous nodes:", previous_nodes)

    
    result_lines.append("\nDistances from start vertex:")
    for vertex, distance in distances.items():
        result_lines.append(f"{vertex}: {distance}")

    result_lines.append("\nPrevious nodes:")
    for vertex, previous in previous_nodes.items():
        result_lines.append(f"{vertex}: {previous}")

    # print the results to the outpt file.<:)>
    with open('Dijkstra_results.txt', 'w') as outfile:
        for line in result_lines:
            outfile.write(line + "\n")

#Greedy:
romania_map = {
    'A': {'B': 3, 'C': 2, 'D': 2},
    'B': {'C': 4, 'E': 4},
    'C': {'D': 6, 'E': 5},
    'D': {'A': 2, 'C': 6},
    'E': {'B': 4,'C': 5},
    
}
# Define the heuristic function as a dictionary
heuristic = {
    'A': 10,
    'B':9,
    'C': 6,
    'D': 5,
    'E': 0,
   
}

def greedy_search(graph, heuristic, start, end):
    total=0
    path = []
    current = start
    while current != end:
        neighbors = graph[current]
        # Choose the neighbor with the lowest heuristic value
        neighbor = min(neighbors, key=lambda x: heuristic[x])
        path.append((current, neighbor))
        current = neighbor
        total = total + neighbors[current]
    return total, path


start = 'A'
end = 'E'
cost, path = greedy_search(romania_map, heuristic, start, end)
print("Total path cost:", cost)
print("Shortest path:", path)



# Aysha Akter Urmi.
# Id: 211000912

# A* Searching Algorithm 


from queue import PriorityQueue
class Graph:
    GRAPH = {'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
             'Zerind': {'Oradea': 71, 'Arad': 75},
             'Oradea': {'Sibiu': 151},
             'Sibiu': {'Rimniciu Vilcea': 80, 'Fagaras': 99, 'Arad': 140},
             'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
             'Rimniciu Vilcea': {'Pitesti': 97, 'Craiova': 146, 'Sibiu': 80},
             'Timisoara': {'Lugoj': 111, 'Arad': 118},
             'Lugoj': {'Mehadia': 70},
             'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
             'Dobreta': {'Mehadia': 75, 'Craiova': 120},
             'Pitesti': {'Craiova': 138, 'Bucharest': 101},
             'Craiova': {'Pitesti': 138, 'Dobreta': 120, 'Rimniciu Vilcea': 146},
             'Bucharest': {'Giurgiu': 90, 'Urziceni': 85, 'Fagaras': 211, 'Pitesti': 101},
             'Giurgiu': {'Bucharest': 90},
             'Urziceni': {'Vaslui': 142, 'Hirsova': 98, 'Bucharest': 85},
             'Vaslui': {'Lasi': 92, 'Urziceni': 142},
             'Lasi': {'Neamt': 87, 'Vaslui': 92},
             'Neamt': {'Lasi': 87},
             'Hirsova': {'Eforie': 86, 'Urziceni': 98},
             'Eforie': {'Hirsova': 86}
             }
    @staticmethod
    def a_star(source, destination):
        heuristics = {'Arad': 366,
                      'Bucharest': 0,
                      'Craiova': 160,
                      'Dobreta': 242,
                      'Eforie': 161,
                      'Fagaras': 176,
                      'Giurgiu': 77,
                      'Hirsova': 151,
                      'Lasi': 226,
                      'Lugoj': 244,
                      'Mehadia': 241,
                      'Neamt': 234,
                      'Oradea': 380,
                      'Pitesti': 100,
                      'Rimniciu Vilcea': 193,
                      'Sibiu': 253,
                      'Timisoara': 329,
                      'Urziceni': 80,
                      'Vaslui': 199,
                      'Zerind': 374
                      }


        pq, visited = PriorityQueue(), {}


        pq.put((heuristics[source], 0, source, [source]))



        while not pq.empty():
            (heuristic, cost, vertex, path) = pq.get()


            if vertex == destination:
                return heuristic, cost, path
            for next_node in Graph.GRAPH[vertex].keys():
                current_cost = cost + Graph.GRAPH[vertex][next_node]
                heuristic = current_cost + heuristics[next_node]
                if next_node not in visited or visited[next_node] >= heuristic:
                    visited[next_node] = heuristic
                    pq.put((heuristic, current_cost, next_node, path + [next_node]))


    @staticmethod
    def main():
        # Take input from User
        source = str(input("Enter a source node: "))
        destination = str(input("Enter a destination node: "))


        heuristic, cost, optimal_path = Graph.a_star(source, destination)


        print("\nPathway of traversal: ")
        print('->'.join(city for city in optimal_path))
        print("\nTotal cost: ", cost)
Graph.main()





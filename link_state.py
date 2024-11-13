import heapq

class LinkStateRouter:
    def __init__(self, router_id, neighbors):
        self.router_id = router_id
        self.neighbors = neighbors
        self.distance_vector = {self.router_id: 0}

    def calculate_shortest_path(self, network_topology):
        unvisited = {node: float('inf') for node in network_topology}
        unvisited[self.router_id] = 0
        visited = {}
        path = {}

        while unvisited:
            min_node = min(unvisited, key=unvisited.get)
            visited[min_node] = unvisited[min_node]
            if visited[min_node] == float('inf'):
                break

            for neighbor, cost in network_topology[min_node].items():
                if neighbor not in visited:
                    new_cost = visited[min_node] + cost
                    if new_cost < unvisited[neighbor]:
                        unvisited[neighbor] = new_cost
                        path[neighbor] = min_node

            unvisited.pop(min_node)

        self.distance_vector = visited
        return visited

def link_state_routing_simulation(network_topology):
    routers = {}
    for router_id, neighbors in network_topology.items():
        routers[router_id] = LinkStateRouter(router_id, neighbors)

    for router_id, router in routers.items():
        shortest_paths = router.calculate_shortest_path(network_topology)
        print(f"Router {router_id} Shortest Paths: {shortest_paths}")

def main():
    network_topology = {}
    num_routers = int(input("Enter the number of routers: "))

    for _ in range(num_routers):
        router_id = input("Enter router ID (e.g., R1, R2): ")
        num_neighbors = int(input(f"Enter the number of neighbors for {router_id}: "))
        neighbors = {}

        for _ in range(num_neighbors):
            neighbor_id = input(f"Enter neighbor router ID for {router_id}: ")
            cost = int(input(f"Enter cost to reach {neighbor_id} from {router_id}: "))
            neighbors[neighbor_id] = cost

        network_topology[router_id] = neighbors

    print("\nLink State Routing Simulation\n")
    link_state_routing_simulation(network_topology)

if __name__ == "__main__":
    main()


"""
Enter the number of routers: 3
Enter router ID (e.g., R1, R2): R1
Enter the number of neighbors for R1: 2
Enter neighbor router ID for R1: R2
Enter cost to reach R2 from R1: 1
Enter neighbor router ID for R1: R3
Enter cost to reach R3 from R1: 4
Enter router ID (e.g., R1, R2): R2
Enter the number of neighbors for R2: 2
Enter neighbor router ID for R2: R1
Enter cost to reach R1 from R2: 1
Enter neighbor router ID for R2: R3
Enter cost to reach R3 from R2: 2
Enter router ID (e.g., R1, R2): R3
Enter the number of neighbors for R3: 2
Enter neighbor router ID for R3: R1
Enter cost to reach R1 from R3: 4
Enter neighbor router ID for R3: R2
Enter cost to reach R2 from R3: 2

Link State Routing Simulation

Router R1 Shortest Paths: {'R1': 0, 'R2': 1, 'R3': 3}
Router R2 Shortest Paths: {'R2': 0, 'R1': 1, 'R3': 2}
Router R3 Shortest Paths: {'R3': 0, 'R2': 2, 'R1': 3}
"""
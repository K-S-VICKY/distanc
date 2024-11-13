import heapq

class DistanceVectorRouter:
    def __init__(self, router_id, neighbors):
        self.router_id = router_id
        self.neighbors = neighbors
        self.distance_vector = {self.router_id: 0}
        for neighbor, cost in neighbors.items():
            self.distance_vector[neighbor] = cost

    def update_distance_vector(self, received_vector, sender):
        updated = False
        for node, dist in received_vector.items():
            new_distance = self.neighbors[sender] + dist
            if node not in self.distance_vector or new_distance < self.distance_vector[node]:
                self.distance_vector[node] = new_distance
                updated = True
        return updated

    def send_update(self):
        for neighbor in self.neighbors:
            send_to_neighbor(self.router_id, neighbor, self.distance_vector)

def distance_vector_routing_simulation(network_topology):
    routers = {}
    for router_id, neighbors in network_topology.items():
        routers[router_id] = DistanceVectorRouter(router_id, neighbors)
    for router in routers.values():
        router.send_update()
    for router in routers.values():
        print(f"Router {router.router_id} Distance Vector: {router.distance_vector}")

def send_to_neighbor(sender_id, neighbor_id, distance_vector):
    print(f"Router {sender_id} sends distance vector to Router {neighbor_id}")

def main():
    # Get input for the network topology
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

    # Run Distance Vector Routing simulation
    print("\nDistance Vector Routing Simulation\n")
    distance_vector_routing_simulation(network_topology)

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

Distance Vector Routing Simulation

Router R1 sends distance vector to Router R2
Router R1 sends distance vector to Router R3
Router R2 sends distance vector to Router R1
Router R2 sends distance vector to Router R3
Router R3 sends distance vector to Router R1
Router R3 sends distance vector to Router R2

Router R1 Distance Vector: {'R1': 0, 'R2': 1, 'R3': 3}
Router R2 Distance Vector: {'R2': 0, 'R1': 1, 'R3': 2}
Router R3 Distance Vector: {'R3': 0, 'R1': 3, 'R2': 2}
"""
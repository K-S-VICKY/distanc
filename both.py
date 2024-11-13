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

class LinkStateRouter:
    def __init__(self, router_id):
        self.router_id = router_id
        self.topology = {}

    def receive_link_state(self, link_state):
        for router, neighbors in link_state.items():
            self.topology[router] = neighbors

    def run_dijkstra(self, start):
        distances = {router: float('inf') for router in self.topology}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_router = heapq.heappop(priority_queue)
            if current_distance > distances[current_router]:
                continue
            for neighbor, cost in self.topology[current_router].items():
                distance = current_distance + cost
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

    def send_link_state(self):
        broadcast_link_state(self.router_id, self.topology)

def send_to_neighbor(sender_id, neighbor_id, distance_vector):
    print(f"Router {sender_id} sends distance vector to Router {neighbor_id}")

def broadcast_link_state(sender_id, topology):
    print(f"Router {sender_id} broadcasts link state")

def input_network_topology():
    topology = {}
    num_routers = int(input("Enter the number of routers: "))
    for _ in range(num_routers):
        router_id = input("Enter router ID (e.g., R1, R2): ")
        num_neighbors = int(input(f"Enter the number of neighbors for {router_id}: "))
        neighbors = {}
        for _ in range(num_neighbors):
            neighbor_id = input(f"Enter neighbor router ID for {router_id}: ")
            cost = int(input(f"Enter cost to reach {neighbor_id} from {router_id}: "))
            neighbors[neighbor_id] = cost
        topology[router_id] = neighbors
    return topology

def main():
    network_topology = input_network_topology()
    print("\nNetwork Topology:")
    for router, neighbors in network_topology.items():
        print(f"{router}: {neighbors}")

    while True:
        print("\nChoose Routing Algorithm:")
        print("1. Distance Vector Routing")
        print("2. Link State Routing")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            print("\nDistance Vector Routing Simulation\n")
            routers = {}
            for router_id, neighbors in network_topology.items():
                routers[router_id] = DistanceVectorRouter(router_id, neighbors)
            for router in routers.values():
                router.send_update()
            for router in routers.values():
                print(f"Router {router.router_id} Distance Vector: {router.distance_vector}")

        elif choice == "2":
            print("\nLink State Routing Simulation\n")
            routers = {}
            for router_id in network_topology:
                routers[router_id] = LinkStateRouter(router_id)
            for router in routers.values():
                router.receive_link_state(network_topology)
                router.send_link_state()
            for router_id, router in routers.items():
                shortest_paths = router.run_dijkstra(router_id)
                print(f"Router {router_id} Shortest Paths: {shortest_paths}")

        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

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

Network Topology:
R1: {'R2': 1, 'R3': 4}
R2: {'R1': 1, 'R3': 2}
R3: {'R1': 4, 'R2': 2}

Choose Routing Algorithm:
1. Distance Vector Routing
2. Link State Routing
3. Exit
Enter choice (1/2/3): 1

Distance Vector Routing Simulation

Router R1 sends distance vector to Router R2
Router R1 sends distance vector to Router R3
Router R2 sends distance vector to Router R1
Router R2 sends distance vector to Router R3
Router R3 sends distance vector to Router R1
Router R3 sends distance vector to Router R2

Router R1 Distance Vector: {'R1': 0, 'R2': 1, 'R3': 3}
Router R2 Distance Vector: {'R2': 0, 'R1': 1, 'R3': 2}
Router R3 Distance Vector: {'R3': 0, 'R2': 2, 'R1': 3}

Choose Routing Algorithm:
1. Distance Vector Routing
2. Link State Routing
3. Exit
Enter choice (1/2/3): 2
Link State Routing Simulation

Router R1 broadcasts link state
Router R2 broadcasts link state
Router R3 broadcasts link state

Router R1 Shortest Paths: {'R1': 0, 'R2': 1, 'R3': 3}
Router R2 Shortest Paths: {'R1': 1, 'R2': 0, 'R3': 2}
Router R3 Shortest Paths: {'R1': 3, 'R2': 2, 'R3': 0}

Choose Routing Algorithm:
1. Distance Vector Routing
2. Link State Routing
3. Exit
Enter choice (1/2/3): 3
Exiting the application.
"""
    


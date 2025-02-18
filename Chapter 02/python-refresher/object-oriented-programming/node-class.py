# Node class
class Node:
    def __init__(self, name, ip_address, status="healthy"):
        self.name = name
        self.ip_address = ip_address
        self.status = status

    def simulate_network_failure(self):
        self.status = "unreachable"

    def simulate_disk_failure(self):
        self.status = "disk_failure"

    def simulate_cpu_failure(self):
        self.status = "cpu_failure"

node1 = Node("Node 1", "192.168.0.1")
node2 = Node("Node 2", "192.168.0.2")

# Simulate network failure on node1
node1.simulate_network_failure()

# Simulate disk failure on node2
node2.simulate_disk_failure()

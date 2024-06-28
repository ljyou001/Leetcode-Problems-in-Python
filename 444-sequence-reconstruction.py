# lint 605

class Solution:
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph = self.build_graph(seqs)
        topo_order = self.topo_sort(graph)
        return org == topo_order

    def build_graph(self, seqs):
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
        for seq in seqs:
            for i in range(len(seq) - 1):
                graph[seq[i]].add(seq[i + 1])
        return graph
    
    def get_indegree(self, graph):
        indegree = {
            node: 0
            for node in graph.keys()
        }
        for item, val in graph.items():
            for node in val:
                indegree[node] += 1
        return indegree

    def topo_sort(self, graph):
        indegree = self.get_indegree(graph)
        queue = collections.deque()
        for key, val in indegree.items():
            if val == 0:
                queue.append(key)
        topo_order = []
        while queue:
            if len(queue) > 1:
                return None
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return topo_order

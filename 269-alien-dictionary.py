# lint 892
import heapq
class Solution:
    def alien_order(self, words: List[str]) -> str:
        graph, indegree = self.build_graph(words)
        if not graph:
            return ''
        return self.topo_sort(graph, indegree)
 
    def build_graph(self, words):
        graph = {}
        indegree = {}
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()
                    indegree[char] = 0
 
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            length = min(len(word1), len(word2))
            for j in range(length):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]: # 防止入度建错
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
                if j == length - 1:
                    if len(word1) > len(word2):
                        return None, None
        return graph, indegree
 
    def topo_sort(self, graph, indegree):
        queue = [node for node in indegree if indegree[node] == 0]
        heapq.heapify(queue) 
        # heap在这里是为了当没有明确顺序输出英文顺序的。
        res = ''
        while queue:
            char = heapq.heappop(queue)
            res += char
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heapq.heappush(queue, neighbor)
        return res if len(res) == len(graph) else ''
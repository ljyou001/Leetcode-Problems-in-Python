class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:
            return []
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for outnode, innode in prerequisites:
            graph[innode].append(outnode)
            indegree[outnode] += 1
        
        queue = deque([
            i 
            for i in range(numCourses) 
            if indegree[i] == 0
        ])
        
        course_taken = []
        while queue:
            c = queue.popleft()
            course_taken.append(c)
            for course in graph[c]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return course_taken if len(course_taken) == numCourses else []
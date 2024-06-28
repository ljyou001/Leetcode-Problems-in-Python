class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph and get the in degree
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        course_taken = 0
        while queue:
            c = queue.popleft()
            course_taken += 1
            for course in graph[c]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        return course_taken == numCourses
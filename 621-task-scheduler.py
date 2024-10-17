class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        tasks = Counter(tasks)
        heap = []
        for key in tasks.keys():
            heapq.heappush(heap, (tasks[key] * -1, key))
        
        timestamp = 0
        pending_queue = deque() # (avail_time, times, task)
        while heap or pending_queue:
            while pending_queue and pending_queue[0][0] < timestamp:
                _, times, task = pending_queue.popleft()
                heapq.heappush(heap, (times, task))
            if not heap:
                timestamp += 1
                continue
            times, task = heapq.heappop(heap)
            times += 1
            if times < 0:
                pending_queue.append((timestamp + n, times, task))
            timestamp += 1
        return timestamp
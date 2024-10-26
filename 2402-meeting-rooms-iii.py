class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return 0
        
        meetings.sort()
        avail_rooms = [i for i in range(n)] # heap for room num
        end_times = [] # (end time, room number)
        counter = [0 for _ in range(n)]

        for start, end in meetings:
            while end_times and start >= end_times[0][0]:
                _, room_number = heapq.heappop(end_times)
                heapq.heappush(avail_rooms, room_number)

            if not avail_rooms:
                most_rect_end_time, room_number = heapq.heappop(end_times)
                end = most_rect_end_time + (end - start)
                heapq.heappush(avail_rooms, room_number)

            room_number = heapq.heappop(avail_rooms)
            heapq.heappush(end_times, (end, room_number))
            counter[room_number] += 1

        max_index = -1
        max_value = -1
        for i in range(len(counter)):
            if counter[i] > max_value:
                max_value = counter[i]
                max_index = i
        return max_index
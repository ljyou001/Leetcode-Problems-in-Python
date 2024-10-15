from collections import deque

class OutputStatus:
    RES_200 = '{status: 200, message: OK}'
    RES_429 = '{status: 429, message: Too many requests}'

class Solution:
    def solution(self, requests):
        timestamp_dict = {}
        res = []
        for timestamp, req in enumerate(requests):
            if req not in timestamp_dict:
                timestamp_dict[req] = deque([timestamp])
                res.append(OutputStatus.RES_200)
                continue
            
            # Handling 30 sec situation
            while timestamp_dict[req][0] <= timestamp - 30:
                timestamp_dict[req][0].popleft()

            if len(timestamp_dict[req][0]) > 5:
                res.append(OutputStatus.RES_429)
                continue
            
            # Handling 5 sec situation
            five_sec_count = 0
            for times in timestamp_dict[req]:
                if timestamp - times < 5:
                    five_sec_count += 1
            
            if five_sec_count > 2:
                res.append(OutputStatus.RES_429)
                continue
            
            timestamp_dict[req].append(timestamp)
            res.append(OutputStatus.RES_200)
            
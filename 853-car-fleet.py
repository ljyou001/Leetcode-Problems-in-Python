# List method
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        pairs.sort()
        
        car_list = [(target - pairs[-1][0]) / pairs[-1][1]]

        for p, s in pairs[::-1]:
            time = (target - p) / s
            if time > car_list[-1]:
                car_list.append(time)
        
        return len(car_list)
    

# MONOTONIC STACK 

""" The trick is to work from right to left and look at which cars have intersections (that's why we move from right to left!) as well as
    converting the positions and speeds into a single value as the TIME TO DESTINATION for the MONOTONIC stack... 
    MAKE SURE TO SORT THE CARS AND THEN WORK BACKWARDS ON THAT (HENCE GOING FROM RIGHT TO LEFT, OR FARTHEST ALONG CAR TO EARLIEST CAR)
    (?) Check Neetcode again to see why we use an if statement instead of a while loop
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []  # this keeps track of the times to destination! 

        for p, s in sorted(pair)[::-1]:     
        # reverse sorted order! this mimics working from right to left, i.e. cars closest to finish line to farthest 
            # calculate and add time to destination to stack! 
            stack.append((target-p) / s)    

            # if there's at least two cars on the stack AND there's an intersection expected between the FRONT TWO CARS, THEN POP! 
            # we check this by seeing whether the frontmost car is SLOWER THAN OR EQUAL TO the 2nd FRONTMOST CAR 
            # by popping, we're simulating the two cars becoming a fleet! 
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop() 

        # return answer at the end of determining all intersections! 
        return len(stack)
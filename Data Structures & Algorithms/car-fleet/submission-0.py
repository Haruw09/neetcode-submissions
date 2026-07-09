class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse=True)
        fleets = 0
        slowest_time = 0
        for pos, speed in cars:
            time = (target - pos) / speed
            if time > slowest_time:
                fleets += 1
                slowest_time = time
                
        return fleets

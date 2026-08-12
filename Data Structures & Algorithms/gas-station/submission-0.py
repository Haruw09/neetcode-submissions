class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        gas_value = 0
        result = 0
        for i in range(len(gas)):
            gas_value += (gas[i] - cost[i])
            if gas_value < 0:
                gas_value = 0
                result = i + 1

        return result
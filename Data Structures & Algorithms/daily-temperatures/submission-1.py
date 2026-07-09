class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp_num = len(temperatures)
        for i in range(temp_num - 2, -1, -1):
            j = i + 1

            while j < temp_num and temperatures[i] >= temperatures[j]:
                if result[j] == 0:
                    j = temp_num
                    break
                else:
                    j += result[j]
            
            if j < temp_num:
                result[i] = j - i
            
        return result

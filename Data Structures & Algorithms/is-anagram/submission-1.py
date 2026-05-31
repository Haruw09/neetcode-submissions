class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_1 = dict()
        for char in s:
            dict_1[char] = dict_1.get(char, 0) + 1
        for char in t:
            dict_1[char] = dict_1.get(char, 0) - 1
        for value in dict_1.values():
            if value != 0:
                return False
                
        return True

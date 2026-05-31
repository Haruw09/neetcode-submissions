class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = dict()
        for char in s:
            dict_1[char] = dict_1.get(char, 0) + 1
        for char in t:
            dict_1[char] = dict_1.get(char, 0) - 1
        if all(value == 0 for value in dict_1.values()):
            return True
        else:
            return False

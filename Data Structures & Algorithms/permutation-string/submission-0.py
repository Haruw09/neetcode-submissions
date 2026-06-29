class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        for char in s1:
            need[ord(char) - ord('a')] += 1

        window = [0] * 26
        window_length = len(s1)
        for i, char in enumerate(s2):
            window[ord(char) - ord('a')] += 1
            if i >= window_length:
                first_char = s2[i - window_length]
                window[ord(first_char) - ord('a')] -= 1
            if window == need:
                return True
                    
        return False

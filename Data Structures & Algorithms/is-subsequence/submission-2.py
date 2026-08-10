class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True

        word_idx = 0
        for i in range(len(t)):
            if t[i] == s[word_idx]:
                word_idx += 1
                if word_idx == len(s):
                    return True
            
        return False
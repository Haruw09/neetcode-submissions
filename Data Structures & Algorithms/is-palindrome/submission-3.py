class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isalnum():
                if s[r].isalnum():
                    if s[l].lower() != s[r].lower():
                        return False
                    else:
                        r -= 1
                        l += 1
                else:
                    r -= 1
            else:
                l += 1
        return True
            

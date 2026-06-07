class Solution:
    def isPalindrome(self, s: str) -> bool:
        sequence = []
        for char in s:
            if char.isdigit():
                return False
            if char.isalpha():
                sequence.append(char.lower())
        sequence = ''.join(sequence)
        return sequence == sequence[::-1]
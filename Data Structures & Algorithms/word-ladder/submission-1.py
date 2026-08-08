from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0 

        alphabet = [chr(ord('a') + i) for i in range(26)]
        queue = deque([beginWord])
        word_len = len(beginWord)
        depth = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(word_len):
                    for new_char in alphabet:
                        new_word = word[:i] + new_char + word[i + 1:]
                        if new_word in word_set:
                            if new_word == endWord:
                                return depth + 1
                            queue.append(new_word)
                            word_set.remove(new_word)
                        
            depth += 1

        return 0
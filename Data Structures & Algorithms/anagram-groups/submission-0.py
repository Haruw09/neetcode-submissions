class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        patterns = []
        result = []

        for word in strs:
            word_stats = dict()
            for char in word:
                word_stats[char] = word_stats.get(char, 0) + 1
            try:
                i = patterns.index(word_stats)
                result[i].append(word)
            except ValueError:
                patterns.append(word_stats)
                result.append([word])

        return result
                


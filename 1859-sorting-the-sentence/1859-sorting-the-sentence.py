
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        result = [""] * len(words)

        for word in words:
            position = int(word[-1]) - 1
            result[position] = word[:-1]

        return " ".join(result)

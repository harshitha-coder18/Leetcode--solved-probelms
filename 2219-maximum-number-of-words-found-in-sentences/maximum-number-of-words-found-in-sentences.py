class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:

        maximum = 0
        for sentence in sentences:
            count = len(sentence.split())
            if count > maximum:
                maximum = count
        return maximum
           
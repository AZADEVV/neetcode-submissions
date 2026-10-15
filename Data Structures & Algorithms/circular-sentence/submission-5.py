class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        words = sentence.split()

        if len(words) == 1:
            if words[0][0] == words[0][-1]:
                return True
            else:
                return False

        for i in range(len(words) - 1):
            if not words[i][-1] == words[i + 1][0]:
                return False
            
        if words[0][0] == words[-1][-1]:
            return True
        else:
            return False

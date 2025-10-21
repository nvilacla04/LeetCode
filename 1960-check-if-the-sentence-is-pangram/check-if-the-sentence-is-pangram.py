class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counts = set()
        for char in sentence:
            if "a" <= char <= "z":
                counts.add(char)
                if len(counts) == 26:
                    return True
        return len(counts) == 26
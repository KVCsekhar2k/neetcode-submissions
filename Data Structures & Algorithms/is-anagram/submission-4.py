class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        first = sorted(s)
        second = sorted(t)
        if first == second:
            for i in range(len(min(s,t))):
                if first[i] != second[i]:
                    return False
            return True
        return False
        

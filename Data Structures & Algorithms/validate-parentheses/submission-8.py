class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        obj = {'}': '{', ')': '(', ']': '['}
        opening = []
        for chr in s:
            if chr in obj.keys():
                if (len(opening) == 0):
                    return False
                    break
                if obj[chr] == opening[-1]:
                    opening.pop()
                    continue
            opening.append(chr)
        return len(opening) == 0
            


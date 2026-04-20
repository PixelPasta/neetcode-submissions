class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        obj = {'}': '{', ')': '(', ']': '['}
        opening = []
        for chr in s:
            if chr in obj:
                if (not opening):
                    return False
                    break
                if obj[chr] == opening[-1]:
                    opening.pop()
                    continue
            opening.append(chr)
        return len(opening) == 0
            


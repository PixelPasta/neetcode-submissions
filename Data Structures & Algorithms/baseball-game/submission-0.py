class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = [int(operations[0])]
        for i in range(1, len(operations)):
            i = operations[i]
            if i == "+":
                x = ans.pop()
                y = ans.pop()
                ans.extend([y,x,x+y])
            elif i == "C":
                ans.pop()
            elif i == "D":
                ans.append(ans[-1]*2)
            elif str(abs(int(i))).isdigit():
                ans.append(int(i))
        return sum(ans)
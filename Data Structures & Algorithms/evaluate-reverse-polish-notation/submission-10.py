class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for i in range(0, len(tokens)):
            if tokens[i] not in ['/','+','*','-']:
                stack.append(tokens[i])
            # elif tokens[i] in ['+','-','*','/']:
            else:
                x = int(stack.pop())
                y = int(stack.pop())
                if tokens[i] == "+":
                    result = y+x
                elif tokens[i] == "/":
                    result = y/x
                elif tokens[i] == "*":
                    result = y*x
                elif tokens[i] == "-":
                    result = y-x
                stack.append(result)
        return int(stack[0])
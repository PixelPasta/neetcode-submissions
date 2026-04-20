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
                x = stack.pop()
                y = stack.pop()
                result = int(eval(f"{y}{tokens[i]}{x}"))
                stack.append(result)
        return stack[0]
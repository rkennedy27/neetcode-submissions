class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens: 
            if t not in "+-*/":
                stack.append(int(t))
            else: 
                val2 = stack.pop()
                val1 = stack.pop()

                if t == "+":
                    stack.append(val1+val2)
                elif t == "-":
                    stack.append(val1-val2)
                elif t == "*":
                    stack.append(val1*val2)
                elif t=="/":
                    if val2 == 0:
                        stack.append(0)
                    else:
                        stack.append(int(val1/val2))
                
    
        return stack[-1]


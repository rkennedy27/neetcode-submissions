class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}



        for c in s:
            if c in mapping: 

                if not stack:
                    return False
                
                print("stack[-1] : " + stack[-1])
                print("C: " + c)
                print("mapping[c]: " + mapping[c])


                if stack[-1] !=mapping[c]:
                    return False

                stack.pop()
            else: 
                stack.append(c)


        return len(stack) == 0 
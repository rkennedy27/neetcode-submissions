class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #(index, temp)

        for i, t in enumerate(temperatures): #(index, temp)
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index

            stack.append((t,i))

        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n

        left = 1
        right = 1

        #left
        for i in range(n):
            out[i] = left
            left *= nums[i]
        #right
        for i in range(n - 1, -1, -1):
            out[i] *= right
            right *= nums[i]

        return out
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0

        #if cycle they will meet
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        #start new slow at beginneing, meeting point is dupe
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow 
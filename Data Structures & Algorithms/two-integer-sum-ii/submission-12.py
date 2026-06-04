class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(numbers)):
            n = numbers[i]
            diff = target - n

            if diff in mp:
                return [mp[diff], i+1]

            mp[n] = i + 1

        return []
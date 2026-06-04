class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            n = numbers[i]
            tmp = target - n
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[n] = i + 1
        return []
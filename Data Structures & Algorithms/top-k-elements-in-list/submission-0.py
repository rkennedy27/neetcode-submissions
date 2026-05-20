class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print("hello world")
        counts = Counter(nums)
        top = counts.most_common(k)
        result = []
        for num, count in top:
            result.append(num)
        return result
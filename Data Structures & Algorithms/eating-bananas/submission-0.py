class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        k = high

        while low<=high: 
            midpoint = (low+high)//2

            hours = 0
            for pile in piles:
                hours+=math.ceil(pile/midpoint)

            if hours<=h:
                k = midpoint
                high = midpoint -1
            else:
                low = midpoint+1
                
        return k

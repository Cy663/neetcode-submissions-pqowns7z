class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        res = 0
        while l<r:
            diff = heights[l]-heights[r]
            res = max(res,min(heights[l],heights[r])*(r-l))
            if diff>0:
                r-=1
            else:
                l+=1
        return res
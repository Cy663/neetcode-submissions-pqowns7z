class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        res = 0
        left_max,right_max = 0,0
        while l<r:
            left_max = max(left_max,height[l])
            right_max = max(right_max,height[r])
            if left_max<=right_max:
                l+=1
                res+=left_max-height[l-1]
            else:
                r-=1
                res+=right_max-height[r+1]
        return res 
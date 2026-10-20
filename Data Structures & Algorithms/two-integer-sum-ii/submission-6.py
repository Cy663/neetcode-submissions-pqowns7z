class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i,n in enumerate(numbers):
            if n in mp:
                return [mp[n]+1,i+1]
            mp[target-n] = i

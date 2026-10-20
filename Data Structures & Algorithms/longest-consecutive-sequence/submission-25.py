class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i]-1 in num_set:
                continue
            curr = nums[i]
            curr_len = 1
            while curr+1 in num_set:
                curr+=1
                curr_len+=1
            longest = max(longest,curr_len)
        return longest
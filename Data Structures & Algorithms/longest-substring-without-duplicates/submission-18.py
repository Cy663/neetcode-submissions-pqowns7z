class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        curr = set()
        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l+=1
            else:
                res = max(res,r-l+1)
                curr.add(s[r])
        return res
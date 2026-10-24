class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,res = 0,0
        curr = set()
        for r in range(len(s)):
            if s[r] in curr:
                while s[r] in curr:
                    curr.remove(s[l])
                    l+=1
            else:
                res = max(res,r-l+1)
            curr.add(s[r])
        return res
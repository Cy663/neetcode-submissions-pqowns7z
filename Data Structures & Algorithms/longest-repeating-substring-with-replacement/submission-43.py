class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        curr_max = 0
        l=0
        res = 0
        for r,c in enumerate(s):
            count[c] = count.get(c,0)+1
            curr_max = max(curr_max,count[c])
            if r-l+1-curr_max>k:
                count[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res
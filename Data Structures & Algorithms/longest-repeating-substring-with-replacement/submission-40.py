class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=[0]*26
        max_count = 0
        l = 0
        for r in range(len(s)):
            idx = ord(s[r])-ord('A')
            count[idx]+=1
            max_count = max(max_count,count[idx])
            if r-l+1-max_count>k:

                count[ord(s[l])-ord('A')]-=1
                l+=1
        return len(s)-l
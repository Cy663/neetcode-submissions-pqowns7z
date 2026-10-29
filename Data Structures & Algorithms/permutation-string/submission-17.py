class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0]*26
        for c in s1:
            count[ord(c)-97]+=1
        l=0
        for r,c in enumerate(s2):
            idx = ord(c)-97
            count[idx]-=1
            while count[idx]<0:
                count[ord(s2[l])-97]+=1
                l+=1
            if r-l+1==len(s1):
                return True
        return False
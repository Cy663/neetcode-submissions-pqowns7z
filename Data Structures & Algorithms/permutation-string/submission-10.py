class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1),len(s2)
        if m>n: return False
        need,win = [0]*26,[0]*26
        
        for i in range(m):
            need[ord(s1[i])-ord('a')] +=1
            win[ord(s2[i])-ord('a')] +=1
        if need==win: return True

        for r in range(n-m):
            win[ord(s2[m+r])-ord('a')] +=1
            win[ord(s2[r])-ord('a')] -=1

            if win==need:
                return True
        return False

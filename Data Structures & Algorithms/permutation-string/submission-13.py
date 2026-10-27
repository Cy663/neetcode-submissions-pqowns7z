class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1),len(s2)
        if m>n: return False
        need,win = [0]*26,[0]*26

        for i in range(m):
            need[ord(s1[i])-ord('a')]+=1
            win[ord(s2[i])-ord('a')]+=1
        matches = sum(win[i]==need[i] for i in range(26))
        if matches ==26: return True

        for r in range(m,n):
            i = ord(s2[r])-ord('a')
            win[i]+=1
            if win[i]==need[i]:
                matches+=1
            elif win[i]==need[i]+1:
                matches-=1
            
            j = ord(s2[r-m])-ord('a')
            win[j]-=1
            if win[j]==need[j]:
                matches+=1
            elif win[j]==need[j]-1:
                matches-=1
            
            if matches==26:
                return True
        return False
            



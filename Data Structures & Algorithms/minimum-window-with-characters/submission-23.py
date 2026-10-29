class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        missing = len(t)
        l = 0
        best_l,best_len = 0,float("inf")
        for r,c in enumerate(s):
            if count[c]>0:
                missing-=1
            count[c]-=1

            while missing==0:
                if r-l+1<best_len:
                    best_l,best_len = l,r-l+1
                count[s[l]]+=1
                if count[s[l]]>0:
                    missing+=1
                l+=1
        
        return "" if best_len==float("inf") else s[best_l:best_l+best_len]
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            re = [0]*26
            for c in s:
                re[ord(c)-ord('a')]+=1
            re = tuple(re)
            if re not in mp:
                mp[re] = [s]
            else:
                mp[re].append(s)
            
        res = []
        for l in mp.values():
            res.append(l)
        return res
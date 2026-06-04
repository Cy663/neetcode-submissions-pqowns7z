class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = collections.defaultdict(list)
        for s in strs:
            k = [0]*26
            for c in s:
                k[ord(c)-ord('a')]+=1
            mp[tuple(k)].append(s)

        return list(mp.values()) 
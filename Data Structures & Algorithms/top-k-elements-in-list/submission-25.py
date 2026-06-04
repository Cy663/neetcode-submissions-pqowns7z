class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for f in range(len(freq)-1,0,-1):
            for n in freq[f]:
                res.append(n)
                if len(res)==k:
                    return res

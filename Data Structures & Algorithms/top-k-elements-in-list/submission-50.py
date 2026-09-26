class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for n in range(len(nums)+1)]
        for n,c in count.items():
            buckets[c].append(n)
        res = []
        for i in range(len(nums),-1,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res)==k:
                    return res
        return res
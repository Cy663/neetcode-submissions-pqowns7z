class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        for n,c in count.items():
            heapq.heappush(heap,[c,n])
            while len(heap)>k:
                heapq.heappop(heap)
        return [n for _,n in heap]    
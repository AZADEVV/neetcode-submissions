class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            smash = heapq.heappop(heap) - heapq.heappop(heap)
            heapq.heappush(heap, smash)
        return abs(heap[0])
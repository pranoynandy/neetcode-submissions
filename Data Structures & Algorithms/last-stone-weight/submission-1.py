class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first > second:
                val = first - second
                heapq.heappush(stones, -val)
        
        #heapq.heappush(stones, 0)
        stones.append(0)
        return abs(heapq.heappop(stones))
        
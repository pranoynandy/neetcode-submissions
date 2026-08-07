class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heapq.heapify(result)
        for i in points:
            dist = ((i[0]-0)**2)+((i[1]-0)**2)
            res = [-(dist),i]
            heapq.heappush(result, res)
            if len(result) > k:
                heapq.heappop(result)
        results = []
        for i,j in result:
            results.append(j)
        return results

        
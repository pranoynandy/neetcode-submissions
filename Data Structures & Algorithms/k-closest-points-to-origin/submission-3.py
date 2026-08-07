class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point = []
        heapq.heapify(point)
        for i in points:
            dist = (i[0]**2)+(i[1]**2)
            res = [-(dist),i]
            heapq.heappush(point, res)
            if len(point) > k:
                heapq.heappop(point)
                
        results = []
        for i,j in point:
            results.append(j)
        return results

        
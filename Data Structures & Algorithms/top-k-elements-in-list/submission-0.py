class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        res = []
        for i,j in sorted_count.items():
            res.append(i)
            if len(res) == k:
                return res
        
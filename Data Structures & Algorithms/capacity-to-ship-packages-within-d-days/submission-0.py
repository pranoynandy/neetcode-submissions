class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)
        capacity = r
        while l<=r:
            m = l+(r-l)//2
            load,ship = m,1
            for i in weights:
                if load - i < 0:
                    ship += 1
                    load = m
                load -= i
            if ship <= days:
                capacity = min(m, capacity)
                r = m - 1
            else:
                l = m + 1
        return capacity
                

        
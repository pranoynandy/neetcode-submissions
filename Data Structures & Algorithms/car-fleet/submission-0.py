class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        fleet = []

        for p,s in sorted(pair)[::-1]:
            time = (target - p)/s
            if fleet:
                if fleet[-1] >= time:
                    continue
                else:
                    fleet.append(time)
            else:
                fleet.append(time)



        return len(fleet)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #pair = [[p,s] for p,s in zip(position, speed)]
        pairs = {}
        for i in range(len(position)):
            pairs[position[i]] = speed[i]
        pair = sorted(pairs.items(), reverse=True)
        fleet = []

        for p,s in pair:
            time = (target - p)/s
            if fleet:
                if fleet[-1] < time:
                    fleet.append(time)
            else:
                fleet.append(time)



        return len(fleet)
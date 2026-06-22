class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        i,j = 0,len(people)-1
        boat = 0
        while i<=j:
            if limit - people[i] >= people[j] and i!=j :
                j -= 1
            i += 1
            boat += 1
        
        return boat

        
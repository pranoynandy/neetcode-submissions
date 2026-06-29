class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        x = "".join(digits)
        y = str(int(x)+1)
        res = []
        for i in y:
            res.append(i)

        return res
        
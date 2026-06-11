class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in range(len(operations)):
            res = 0
            if operations[i] == '+':
                res = int(score[-1]) + int(score[-2])
                score.append(res)
            elif operations[i] == 'D':
                res = int(score[-1]) + int(score[-1])
                score.append(res)
            elif operations[i] == 'C':
                score.pop()
            else:
                score.append(operations[i])
        result = 0
        for i in score:
            result += int(i)

        return result
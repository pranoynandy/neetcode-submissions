class TimeMap:

    def __init__(self):
        self.keyvalue = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyvalue:
            self.keyvalue[key] = []
        self.keyvalue[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyvalue.get(key, [])
        # for i in values:
        #     if i[1] <= timestamp:
        #         res = max(i[0],res)

        l,r = 0, len(values)-1
        while l<=r:
            m = l + (r-l)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m+1
            else:
                r = m-1
        return res
        

class TimeMap:

    def __init__(self):

        self.store = {} # values atre [value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([value, timestamp])
        print(self.store[key])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        l, r = -1, len(values)

        while r-l > 1:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                l =m
            else:
                r = m
        return values[l][0] if l >= 0  else ''
        

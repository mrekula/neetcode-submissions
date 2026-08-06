class LRUCache:

    def __init__(self, capacity: int):

        self.stack = []
        self.capacity = capacity


    def get(self, key: int) -> int:
        for i in range(len(self.stack)):
            if self.stack[i][0] == key:
                temp = self.stack.pop(i)
                self.stack.append(temp)
                return temp[1]
        return -1


    def put(self, key: int, value: int) -> None:

        for i in range(len(self.stack)):
            if self.stack[i][0] == key:
                temp =self.stack.pop(i)
                temp[1] = value
                self.stack.append(temp)
                return 
        if len(self.stack) == self.capacity:
            self.stack.pop(0)
        self.stack.append([key,value])

  
            

        
        

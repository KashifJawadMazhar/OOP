class Counter:
    def __init__(self,count:int=0) ->None:
        self.count = count
        return None
    def addCount(self) ->None:
        self.count+=1
        return self.count    
    def getCount(self) ->int:
        return self.count
    def zeroCount(self) ->None:
        self.count=0
        return self.count
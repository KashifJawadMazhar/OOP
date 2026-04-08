class CoinAcceptor:
    def __init__(self, amount: int=0, value: float=0.0): 
        self.__amount = amount 

        self.__value = value
    
    def insertCoin(self) -> None:
        self.__amount+= 1
        
    def getAmount(self) ->int :
        return (self.__amount)
    def returnCoins(self) ->int:
        val = (self.__amount)
        self.__amount=0
        return val
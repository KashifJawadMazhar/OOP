class CoinAcceptor:
    __amount: int
    __value: float
    def __init__(self) -> None:
        self.__amount=0
        self.__value=0.0
    def insertCoin (self) -> str:
        self.__amount +=1
        value_of_coin= float(input("What is the value of coin that you inserted?"))
        self.__value +=value_of_coin
        return f"You stored coins of worth {self.__value}."
    def getAmount (self) -> str:
        return f"Amount of coin: {self.__amount}, Value of coin: {self.__value:.2f}"
    def returnCoins (self) -> str:
        amount_now=self.__amount
        value_now=self.__value
        self.__amount=0
        self.__value=0.0
        return f"Amount of coin returned:{amount_now}, Value of coin returned:{value_now:.2f}"
class CoinAcceptor:
    def __init__(self, amount: int = 0, value: float = 0.0):
        self.__amount = amount      # number of coins
        self.__value = value        # total value of coins

    def insertCoin(self, coin_value: float) -> None:
        self.__amount += 1
        self.__value += coin_value

    def getAmount(self) -> int:
        return self.__amount

    def getValue(self) -> float:
        return self.__value

    def returnCoins(self) -> tuple[int, float]:
        coins = self.__amount
        value = self.__value
        self.__amount = 0
        self.__value = 0.0
        return coins, value
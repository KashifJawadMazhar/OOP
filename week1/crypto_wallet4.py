# CryptoWallet class demonstrating encapsulation
class CryptoWallet:
    def __init__(self, walletId):
        # Private attributes (cannot be accessed directly)
        self.__walletId = walletId
        self.__balance = 0.0
        self.__history = []  # Stores transaction history

    def deposit(self, amount):
        # Add money to wallet
        if amount > 0:
            self.__balance += amount
            self.__history.append(f"Deposited {amount}")
            return True
        return False

    def withdraw(self, amount):
        # Withdraw money if balance is enough
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__history.append(f"Withdrew {amount}")
            return True
        return False

    def get_balance(self):
        # Return current balance (read-only)
        return self.__balance

    def get_history(self):
        # Return list of all transactions
        return self.__history

    def get_wallet_id(self):
        # Return wallet ID (read-only)
        return self.__walletId
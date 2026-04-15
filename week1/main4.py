from crypto_wallet4 import CryptoWallet

def main():
    wallets = {}  # Store wallets by ID

    while True:
        print("Menu:")
        print("1 - Create Wallet")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Check Balance")
        print("5 - Transaction History")
        print("0 - Exit")

        choice = input("Your choice: ")

        # Create a new wallet
        if choice == "1":
            walletId = input("Enter Wallet ID: ")
            if walletId in wallets:
                print("Wallet already exists.")
            else:
                wallets[walletId] = CryptoWallet(walletId)
                print("Wallet created.")

        # Deposit
        elif choice == "2":
            walletId = input("Wallet ID: ")
            if walletId in wallets:
                amount = float(input("Amount to deposit: "))
                if wallets[walletId].deposit(amount):
                    print("Deposit successful.")
                else:
                    print("Invalid amount.")
            else:
                print("Wallet not found.")

        # Withdraw
        elif choice == "3":
            walletId = input("Wallet ID: ")
            if walletId in wallets:
                amount = float(input("Amount to withdraw: "))
                if wallets[walletId].withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance or invalid amount.")
            else:
                print("Wallet not found.")

        # Check balance
        elif choice == "4":
            walletId = input("Wallet ID: ")
            if walletId in wallets:
                print("Balance:", wallets[walletId].get_balance())
            else:
                print("Wallet not found.")

        # Transaction history
        elif choice == "5":
            walletId = input("Wallet ID: ")
            if walletId in wallets:
                print("--- Transaction History ---")
                for h in wallets[walletId].get_history():
                    print(h)
            else:
                print("Wallet not found.")

        # Exit
        elif choice == "0":
            print("Program ending.")
            break

        # Invalid menu choice
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
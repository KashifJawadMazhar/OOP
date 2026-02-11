from coin_acceptor import CoinAcceptor

class Main:
    acceptor = CoinAcceptor()
    while True:
        print("\nProgram starting.")
        print("1) Insert coin.")
        print("2) Show the coins.")
        print("3) Return the coins.")
        print("0) Exit program.")
        choice = int(input("What's your choice?"))

        if choice == 1:
            print(acceptor.insertCoin())
        elif choice == 2:
            print(acceptor.getAmount())
        elif choice == 3:
            result = acceptor.returnCoins()
            print(result)
        elif choice == 0:
            print("Program ending.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
if __name__=="__main__":
    Main()
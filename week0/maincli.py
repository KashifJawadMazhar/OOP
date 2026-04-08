from coin_acceptorcli import CoinAcceptor

obj = CoinAcceptor()

print("Program starting.")
print("Welcome to coin acceptor program.")
print("Insert new coin by typing its value (0 returns the money, -1 exits the program)\n")

while True:
    try:
        user = float(input("Insert coin(0 return, -1 exit): "))

        if user == -1:
            print("Exiting program.")
            break

        elif user == 0:
            print("Returning coins...")
            coins, value = obj.returnCoins()
            print(f"{coins} coins with {value}€ value returned.")
            print(f"Inserted coins = {obj.getAmount()}, value = {obj.getValue()}€\n")

        elif user > 0:
            print("Inserting...")
            obj.insertCoin(user)
            print(f"Inserted coins = {obj.getAmount()}, value = {obj.getValue()}€\n")

        else:
            print("Invalid number.\n")

    except ValueError:
        print("Error! Please enter a valid number.\n")

print("Program ending.")
from coin_acceptor import CoinAcceptor
obj = CoinAcceptor()
print(
'''
Program starting.
'''
)
while True:
    print(
'''
1 - Insert coin
2 - Show coins
3 - Return coins
0 - Exit program
'''
    )
    try:
        user = int(input('Choice: '))
        if user==1:
            obj.insertCoin()
        elif user==2:
            print(f"Currently '{obj.getAmount()}' coins in coin acceptor")
        elif user==3:
            print(f"Coin acceptor returned '{obj.returnCoins()}' coins.")
        elif user==0:
            print('Program ending.')
            break
        else:
            print('Invalid choice!')
    except ValueError:
        print('There is some error in your input data.')
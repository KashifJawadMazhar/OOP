from counter import Counter
class Main:
    def __init__(self):
        print(
'''Program starting.
Initializing counter...
Counter initialized.
''')
        self.converter = Counter()
    def run(self):
        while True:
            print(
'''Options:
1) Add count
2) Get count
3) Zero count
0) Exit program''')
            choice = int(input("Choice: "))
            if choice==1:
                print("Count increased")
                self.converter.addCount()
            elif choice==2:
                print(f"Current count '{self.converter.getCount()}'")
            elif choice==3:
                print("Count zeored")
                self.converter.zeroCount()
            elif choice==0:
                print("\nProgramme ending.")
                break
if __name__=="__main__":
    object = Main()
    object.run()
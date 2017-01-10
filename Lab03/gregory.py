# gregory.py
#    Program to compute the Gregorian epact.


def main():
    print("This program calculates the Gregorian Epact.")
    year=eval(input("Enter a 4-digit year: "))
    C=int(year)//100
    
    epact=(8+(C//4)-C+((8*C+13)//25)+11*(year%19))%30
    print(int(epact))

main()



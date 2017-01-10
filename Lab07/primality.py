##Program that outputs the first number it encounters that divides by x
#or outputs that it is a prime number
#primality.py
#By:Piranaven Selvathayabaran

from math import*
def main():
    n=eval(input("Enter a number, and this program will tell if it is a prime number or not: " ))
    x=int(sqrt(n))
    y=2
    if n==1:
        print("This is not a prime number")
    elif n == 2:
        print("This is a prime number")
    else:
        while y<=x and n%y!=0:
            y=y+1
        if n%y==0:
            print("This is not a Prime Number, it divides by ",y)
        else:
            print("This is a prime number")

main()    


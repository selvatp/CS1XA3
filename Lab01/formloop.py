# File:formloop.py
#simple program that executes a for-loop 10 times (0-9)
#and prints the answer to e^x, where x is a number from 0 to 9. 
 
import math 

def main():
    for i in range(10):
        x=math.exp(i)
        print(x)
main()

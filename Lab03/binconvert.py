##binconvert.py
## This program outputs the decimal value of a binary number
## By : Piranave Selvathayabaran

def main():
    NumOfBits=eval(input("Enter the number of binary terms you would like to convert: "))
    y=0
 
    for i in range(NumOfBits):
        bit=eval(input("Enter the bit (0 or 1) : "))
        answer= (2**(i))*bit
        y=y+answer
    print(int(y))

main()    



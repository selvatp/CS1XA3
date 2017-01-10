##Program that takes a list of numbers and returns the biggest of them.
##  By: Piranaven Selva


## Recursive

def max(L):
    
    if len(L) == 1:
        return L[0]
    else:
        m = max(L[1:])
        return m if m > L[0] else L[0]

def main():
    L = eval(input("Please enter a list of numbers: "))
    L=list(L)
    print("The largest number is: ", max(L))

main()


##Program that takes a list of numbers and returns the biggest of them.
##  By: Piranaven Selva

##NON-RECURSIVE

def max(L):

    base=0
    for i in range(len(L)):
        if L[i-1]>=base:
            base=L[i-1]
            
    return base   
    
    


def main():
    L = eval(input("Please enter a list of numbers: "))
    L=list(L)
    maxx=max(L)
    print("The largest number is: ", maxx)
main()

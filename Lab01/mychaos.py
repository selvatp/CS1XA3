#File:mychaos.py
#simple program that illustrates chaotic behaviour given a number between 0 and 1 and a number of results wanted.

def main():
    print("Chaotic function")
    x=eval(input("Enter a number between 0 and 1:"))
    z=eval(input("Enter a second number between 0 and 1:"))
    n=eval(input("How many numbers should I print:")) 
    for i in range(n):
        x=3.9*x*(1-x)
        z=3.9*z*(1-z)
        print(x,"     ",z)
        
    
    
        
        
        
main()

#iterfib.py 
##Program to calulatge n values of Fibonacci sequence
## By : Piranave Selvathayabaran

def main():

    n=eval(input("Enter the number of values in the Fibonnaci sequence you would like to compute: "))
    fib1=1
    fib2=1
    for i in range(n-2):
      fib1,fib2=fib2,fib1+fib2

    print(fib2)

main()

     

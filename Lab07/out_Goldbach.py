##Program that computes Goldbachs conjecture 
##out_Goldbach.py

import math
 
##Check if provided number is Prime of not by sending pCheck value back.
## pCheck = 1 : PRIME
## pCheck = 0 : Not PRIME
def primeCheck(pPossible):
    test = 2
    half = math.sqrt(pPossible)
    pCheck = 1                  # in fist few small number 2,3 HALF is less than test so
                                # it wont go inside loop at all!
                                # must set pCheck = 0 to fix this
     
    while test <= half:
                  
        if pPossible%test == 0:             # Evenly divided, NOT Prime!        
            pCheck = 0                      # Break out and report its not prime
            break
        else:
            test = test+1                   # Get next number to re-check if its prime
                                            # for real Prime it will continue +1 until
                                            # over HALF value and loop end.
                                             
    if pPossible%test != 0:                 # Last check to see if pPosible is Prime   
        pCheck = 1                          # so mark the report pCHECK
 
    return pCheck
 
 
 
#Middle man, Use for create Prime List up to user enter MAX number.
# it will call primeChecker() to check each number and put inside List
def primeLister(max):
    pPossible = 2
    pList = []
     
    # find PRIME number up to Max   
    while pPossible < max:                
         
        pCheck = primeCheck(pPossible)
 
        if pCheck == 1:
            pList.append(pPossible)
                 
        pPossible = pPossible+1
                
    return pList    
 
 
 
 
def main():
    print('Goldbach Conjecture Calculator\n')
    
    
        # Ask for number, must be positive integer over 2!
    while True:
        n = eval(input('Please enter a value over 2:'))
        if n%2 == 0 and n > 2: break            
        print('That\'s not correct. Try again!\n')

    outfileName="12.txt"
    outfile=open(outfileName,"w")
             
        # Create PRIME LIST up to user number
    pList = primeLister(n)
         
        # Now pick up each item and minus user number
        # check the remain value thats is it a prime or not?
    for i in pList:
        remain = n - i
        pCheck = primeCheck(remain)
             
            # When find the remain thats is prime then quit
        if pCheck == 1: break         
         
    # Print result
    print(i,",",remain)
    print(i,",",remain,file=outfile)
 



  

main()

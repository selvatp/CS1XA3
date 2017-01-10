##Recursive Function to print out the digits of a number in English
## By: Piranaven Selva 
##NumToEng.py


def Numtoeng(Number):
    English = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
              5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

    Number=str(Number)
    if len(Number) == 0:            
      return
    else:
        first = int(Number[0])         
        english = English[first]
        print(english, end= " ")
        Numtoeng(Number[1:])
 


    

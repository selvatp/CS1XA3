## remainder.py
## Program that computes the prefix-remainder of two strings
##By: Piranaven Selvathayabaran




## Assumption: user will type his larger string first based on what program asks




def main():

    str1=input("Enter your first string, your bigger string :  ")
    str2=input("Enter a second string, you smaller string :  ")
    lenstr1=len(str1)
    lenstr2=len(str2)
    lenofstring=lenstr1-lenstr2

    print("Your prefix remainder is ", str1[:lenofstring])
    
main()
    


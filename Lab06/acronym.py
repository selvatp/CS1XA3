##acronym.py
##By:Piranaven Selvathayabaran
##Takes a phrase as input and prints an Acronymn

def main():
    x=input("Enter a sentence you would like to abbreviate: ")
    acro=""
    y=x.split()
    i=0
    while i < len(y):
        z=y[i]
        acro=acro+z[0]
        i=i+1
            
    print("Your abbreviation is : ", acro.upper())

main()


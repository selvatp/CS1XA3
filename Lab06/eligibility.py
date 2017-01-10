##eligibility.py
##By:Piranaven Selvathayabaran 
##Program that accepts someones age and years of citizenship
## and outputs their eligibility for the US Senate and House of Representatives




def main():
    print("This program determines your eligibilty for the Senate and House.")
    years=eval(input("Enter your age : "))
    citizen=eval(input("Enter how long you have been a US citizen: "))

    if years>=30:
        if citizen>=9:
            print("You are eligible to be a US senator and a US Representative!")
        elif citizen>=7:
            print("You are eligible to be a s US Represenative!")
        else:
            print("You are not eligible for the Senate and House. ")
    elif years>=25:
        if citizen>=7:
            print("You are eligible to be a s US Represenative!")
        else:
           print("You are not eligible for the Senate and House. ")
    else:
           print("You are not eligible for the Senate and House. ")
    

main()
        

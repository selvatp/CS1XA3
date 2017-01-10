##seconym.py
##Program that takes the second letter of each word and turns it into a acronym.
##By: Piranaven Selvthayabaran

def main():
    x=input("Enter a sentence you would like to turn into a seconym: ")
    acro=""
    for i in x.split():
        acro=acro+i[1]
    print("Your seconym is : ", acro.upper())

main()

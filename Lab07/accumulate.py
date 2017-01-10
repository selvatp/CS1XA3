##Program that reads a file and accumulates two variables based on conditions provided
##accumulate.py
##By:Piranaven Selvathayabaran 

def main():
    infileName=input("What is the file name? : ")
    infile=open(infileName,"r")
    below=0
    above=0

    for line in infile:
        x=eval(line)
        if x < 67:
            below =below + (67-x)
        elif x > 82:
            above=above+(x-82)

    print("Above = ",above)
    print("Below = ",below)
main()

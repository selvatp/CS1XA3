##Program that outputs the truth table for A and B
##table.py
##By:Piranaven Selva

def main():

    print(" A  B     A and B")
    print("__________________")
    tlist=[True,False]

    for i in range(4):
    
        if i == 0:
            A=True
            x="T"
            B=True
            y=("T")
        elif i == 1:
            A=True
            x="T"
            B=False
            y=("F")
        elif i ==2:
            A=False
            x="F"
            B=True
            y=("T")
        elif i ==3:
            A=False
            x="F"
            B=False
            y="F"

        AB= bool(A and B)
        if AB== True:
            z="T"
        else:
            z="F"
        print("{0}  {1}        {2} ".format(x,y,z))
            
    
main()

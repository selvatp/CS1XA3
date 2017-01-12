#loopa.py

#     A program that asks the user for an expression
#   and then prints out the value of the expression up to 7 times.

#By: Piranaven Selvathayabaran

def main():
    for i in range(7):
        x=eval(raw_input("Give me an expression: "))

        print(x)

main()

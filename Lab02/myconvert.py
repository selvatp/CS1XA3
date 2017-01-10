# myconvert.py

#     A program to convert Celsius temperatures to Fahrenheit and
#     prints a table of Celsius temperatures and the Fahrenheit equivalents
#     every 8 degrees from 0C to 100C

# by: Piranaven Selvathayabaran

def main():
    print("Celsius    |   Fahrenheit")
    for i in range(0,101,8):
        fahrenheit = 9/5 * i + 32
        print(i,"           ",fahrenheit)

main()

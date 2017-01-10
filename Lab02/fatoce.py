# fatoce.py

#     A program to convert Fahrenheit temperatures to Celsius

# by: Piranaven Selvathayabaran

def main():
    print("This program converts the temperature in Fahrenheit to Celsius")
    fahrenheit=eval(input("What is the Fahrenheit temperature ?"))
    celsius=(fahrenheit-32)*(5/9)
    print("The temperature is",celsius,"degrees celsius")

main()

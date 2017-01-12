# fatoce.py

#     A program to convert Fahrenheit temperatures to Celsius

# by: Piranaven Selvathayabaran

def main():
    print("This program converts the temperature in Fahrenheit to Celsius")
    fahrenheit=eval(raw_input("What is the Fahrenheit temperature ?"))
    celsius=(fahrenheit-32.0)*(5.0)/(9.0)
    print("The temperature is",celsius,'degrees celsius')

main()

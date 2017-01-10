##good.py
##By:Piranaven Selvathayabaran 
##

def main():
    try:
        x=(input("Enter a date in the form: day/month/year: "))
        day,month,year =x.split("/")
        day=int(day)
        month=int(month)
        year=int(year)

        
        if 1<=day<=31 and month == 1:
            print("The date is valid")
        elif 1<=day<=31 and month == 3:
            print("The date is valid")
        elif 1<=day<=31 and month == 5:
            print("The date is valid")
        elif 1<=day<=31 and month == 7:
            print("The date is valid")
        elif 1<=day<=31 and month ==8 :
            print("The date is valid")
        elif 1<=day<=31 and month == 10:
            print("The date is valid")
        elif 1<=day<=31 and month == 12:
            print("The date is valid")
        
        elif 1<=day<=30 and month == 4:
            print("The date is valid")
        elif 1<=day<=30 and month == 6:
            print("The date is valid")
        elif 1<=day<=30 and month == 9:
            print("The date is valid")
        elif 1<=day<=30 and month == 11:
            print("The date is valid")
        
        elif 1<=day<=29 and month == 2:
            print("The date is valid")
        
        else:
            print("The date is not correct, try again")

      

    except NameError:
        print("You didn't enter a number")
    except TypeError:
        print("Your input was not a number")
    except SyntaxError:
        print("Your input was not in the correct form ")
    except:
        print("Something went wrong, sorry! Check if you typed in the correct form with the slashes: day/month/year")

    print()
    
    main()

main()
    

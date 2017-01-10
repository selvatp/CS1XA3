## dateconvert2 program with string formating to get rid of the auxiliary string
## variables date1 and date2 

def main():
    # get the day month and year
    day, month, year = eval(input("Please enter day, month, and year numbers: "))

   

    months = ["January", "February", "March", "April", 
              "May", "June", "July", "August", 
              "September", "October", "November", "December"]
    monthStr = months[month-1]


    print("The date is {0:2}/{1:2}/{2:4} or {3:9}{4:2},{5:4} ".format(month,day,year,monthStr,day,year))

main()

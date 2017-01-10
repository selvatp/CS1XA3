##grades.py
##BY:PIRANAVEN SELVATHAYABARAN 
##Program that accepts an exam score and calculates the corresponding
##letter grade.

def main():
    grade=eval(input("Enter your exams score: "))
    if 0<= grade <=49:
        mark='F'
    elif 50<= grade <=59:
        mark='D'
    elif 60<= grade <=69:
        mark='C'
    elif 70<= grade <=79:
        mark='B'
    elif 80<= grade <=100:
        mark='A'
    else:
        print("Invalid entry, please try again witha  number between 0-100 ")

        main()
    
    print("The letter grade of your exam score is: ",mark)
main()

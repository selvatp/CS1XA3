# distance.py
# Program that computes the distance between two points

from math import*

def main():
    print("This program calculates th distance between two coordinates.")
    cx1,cy1=eval(input("Please enter the first coordinate point (x1,y1): "))
    cx2,cy2=eval(input("Please enter the second coordinate point (x2,y2): " ))

    distance=(sqrt(((cx2-cx1)**2)+((cy2-cy1)**2)))
    float(distance)

    print("The distance between the two points is : ",distance)

main()


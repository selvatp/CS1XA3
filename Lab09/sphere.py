## Program that reprsentes the geometric solid sphere 
## By: Piranaven Selvathayabaran

from math import*
class Sphere:

    def __init__(self,radius):
        self.r=radius 

    def getRadius(self):
        return self.r

    def surfaceArea(self):
        return 4*pi*(self.r**2)

    def volume(self):
        return (4/3)*pi*(self.r**3)

def main():

    print("This program calculates the Surface Area and Volume of a sphere:")
    print()
    radius=eval(input ("Please enter the radius: "))
     
    x = Sphere(radius)
    print() 
    print('Volume is:',x.volume())
    print('Area is:',x.surfaceArea())

if __name__ == '__main__': main()

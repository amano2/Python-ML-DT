a1=int(input("Enter side1: "))
a2=int(input("Enter side2: "))
a3=int(input("Enter side3: "))
if(a1==a2==a3):
    print("Equilateral Triangle")
elif(a1==a2|a2==a3|a1==a3):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
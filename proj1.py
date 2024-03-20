Income=int(input("Enter the income amout (in $): "))
tax=0
if(Income<=10000):
    tax=Income*0.1
elif(10000<Income<50000):
    tax=Income*0.15
elif(50000<Income<100000):
    tax=Income*0.2
else:
    tax=Income*0.25
print("Tax amount is",tax)
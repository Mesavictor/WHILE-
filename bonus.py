a=float(input("Enter your salary: "))
b=int(input("Enter your years of service: "))
if b>10:
    print("Net bonus=",0.1*a)
elif b>=6 and b<=10:
    print("Net bonus=",0.08*a)
else:
    print("Net bonus=",0.05*a)
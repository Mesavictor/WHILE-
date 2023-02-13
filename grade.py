while True:
    a=int(input("Enter marks for subject 1: "))
    if a > 0 and a<=100:
        break
while True:
    b=int(input("Enter marks for subject 2: "))
    if b > 0 and b<=100:
        break
while True:
    c=int(input("Enter marks for subject 3: "))
    if c > 0 and c<=100:
        break
average=(a+b+c)/3
if average>70:
    print("Grade=A")
elif (average>=60 and average<70):
    print("Grade=B")
elif (average>=50 and average<60):
    print("Grade=C")
elif (average>=40 and average<50):
    print("Grade=D")
else:
    print("Grade=FAIL")
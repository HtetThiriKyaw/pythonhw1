age = int(input("How old are you ?"))

if age > 85 and age <= 100:
    print("Very old")
if age > 60 and age <= 85:
    print("old")
if age > 40 and age <= 60:
    print("Very Adult")
if age > 30 and age <= 40:
    print("Adult")
if age > 20 and age <= 30:
    print("young")
if age > 10 and age <= 20:
    print("Teenager")
if age >= 1 and age <= 10:
    print("Baby")
if age > 100 or age < 1:
    print("Invalid age!")
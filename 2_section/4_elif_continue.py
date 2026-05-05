age = int(input("How old are you ?"))

if age > 85 and age <= 100:
    print("Very old")
elif age > 60 and age <= 85:
    print("old")
elif age > 40 and age <= 60:
    print("Very Adult")
elif age > 30 and age <= 40:
    print("Adult")
elif age > 20 and age <= 30:
    print("young")
elif age > 10 and age <= 20:
    print("Teenager")
elif age >= 1 and age <= 10:
    print("Baby")
else:
    print("Invalid age!")
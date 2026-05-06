f = int(input("Enter any number?"))

for n in range (1,10) :
    print(n)
    if n == f :
        print("Number Found")
        break
else:
    print("Number not found")
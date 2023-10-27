x = int(input("enter a number : "))

if x == 0 or x==1 :
    print("the number is not prime")
for s in range(2,x):
    if x % s == 0 :
        print("the number is not prime")
        break
    else : 
        print("the number is prime ")
        break
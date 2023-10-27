a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the Third Number : "))

if a < b and b < c :
    print("the minimum number is the first number ", a)
elif b < a and b < c :
    print("the minimum number is the second number ", b)
elif b > a and c >a :
    print("the minimum number is the first number ", a)
elif a < b and c < a :
    print("the minimum number is the third number ", c)
elif c < a and c < b : 
    print("the minimum number is the third number ", c)
elif a == b or b ==c or c == a :
    print("the numbers must be difrent")
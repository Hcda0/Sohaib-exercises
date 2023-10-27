avg = float(input("enter your average : "))

if avg < 10 :
    print("student postponed")
elif avg >= 10 and avg <= 11.99 :
    print("passable")
elif avg >= 12 and avg <= 13.99 :
    print("fairly good")
elif avg >= 14 and avg <= 15.99 :
    print("good")
elif avg >= 16 and avg <= 17.99 :
    print("very good")
elif avg >= 18 :
    print("excelent")
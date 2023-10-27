v = []
nstri = 0
q = 1
x = input("enter a number : ")
for s in x :
    v.insert(-q,s)
    q += 1
strnum = ""
for sn in v :
    strnum = strnum + str(sn)
print(strnum)
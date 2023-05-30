a=eval(input("enter numbers in list"))
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
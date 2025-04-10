def createlist(l,n):
    for i in range(n):
        temp=int(input("enter no"))
        l.append(temp)
    return l
l1=[]
l2=[]
l3=[]
n1=int(input("enter limit1"))
l1=createlist(l1,n1)
print(l1)
n2=int(input("enter limit2"))
l2=createlist(l2,n2)
print(l2)
n3=int(input("enter limit3"))
l3=createlist(l3,n3)
print(l3)

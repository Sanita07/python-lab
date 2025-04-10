def createlist(l,n):
    l=[]
    for i in range(n):
        temp=int(input("enter no"))
        l.append(temp)
    return l
def evensum(l):
    esum=0
    for i in range(len(l)):
        if(i%2==0):
            esum+=l[i]
    return esum
def oddsum(l):
    eodd=0
    for i in range(len(l)):
        if(i%2!=0):
            eodd+=l[i]
    return eodd      
l1=[]
l2=[]
l3=[]
n1=int(input("enter limit1:"))
l1=createlist(l1,n1)
print(l1)
n2=int(input("enter limit2:"))
l2=createlist(l2,n2)
print(l2)
n3=int(input("enter limit3:"))
l3=createlist(l3,n3)
print(l3)
esum1=evensum(l1)
esum2=evensum(l2)
esum3=evensum(l3)
print(esum1,esum2,esum3)
osum1=oddsum(l1)
osum2=oddsum(l2)
osum3=oddsum(l3)
print(osum1,osum2,osum3)
Esum=esum1+esum2+esum3
print(Esum)
Eodd=osum1+osum2+osum3
print(Eodd)
SUMMATION=Esum*Eodd
print(SUMMATION)

d={}
for i in range(2):
    key=int(input("Enter key:"))
    value=input("Enter value:")
    d[key]=value
    
print("Value in the dictionary is:")
for i in d:
    print(d[i])
    print(i)

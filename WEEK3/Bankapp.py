def credit(Bal,value):
    Bal+=value
    return Bal
def debit(Bal,value):
    Bal-=value
    return Bal
def checkbalance(Bal):
    print("Check Balance:",Bal)
Bal=0
Bal=credit(Bal,1000)
print( "Amount credited:",Bal)
Bal=debit(Bal,200)
print( "Amount debited:",Bal)
checkbalance(Bal)

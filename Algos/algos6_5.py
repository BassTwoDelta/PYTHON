def coins(amountInCents):
    q = 0
    d = 0
    n = 0
    p = 0
    count = 0
    
    for i in range(0,amountInCents-24,25):
        q += 1
        count += 25
    for i in range(count, amountInCents-9,10):
        d += 1
        count += 10 
    for i in range(count, amountInCents-4, 5):
        n =+ 1
        count += 5 
    for i in range(count, amountInCents,1):
        p += 1 
        count += 1
    print(q,d,n,p)
    newObj = {"Quarters":q,"Dimes":d,"Nickels":n,"Pennies":p}
    print(newObj)
    
print(coins(87))
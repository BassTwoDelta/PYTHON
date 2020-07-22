def parensV(stringInput):
    Ocount = 0
    Ccount = 0
    for i in range(0,len(stringInput),1):
        if stringInput[i] == "(":
            Ocount += 1 
        if stringInput[i] == ")":
            Ccount += 1
        if Ccount > Ocount: 
            return False
    if Ocount == Ccount: 
        return True 
    else:
        return False 
    
print(parensV("((()))("))


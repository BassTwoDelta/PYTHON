
# def isPal(stringInput):
#     newstr = ""
#     for i in range(len(stringInput)-1,-1,-1):
#         newstr += stringInput[i]
#     if newstr == stringInput:
#         return True
#     else:
#         return False


# print(isPal("racecar"))

def isPal(stringInput): 
    for i in range(0,len(stringInput)/2,1):
        if stringInput[i] != stringInput[len(stringInput)-i-1]: 
            return False
    return True

print(isPal('racecar'))
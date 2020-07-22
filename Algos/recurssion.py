# def sigma(numInput): 
#     #code here
#     if numInput <=0:
#         return 0
#     elif numInput ==1:
#         return 1
#     else:
#         return numInput + sigma(numInput-1)

# print(sigma(4)) 

# def factorial(numInput):
#     num = int(numInput)
#     if num <=0:
#         return 1
#     elif num ==1:
#         return 1
#     else: 
#         return num * factorial(num-1)

# print(factorial(6.5))

# def getNthFib(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else: 
#         return getNthFib(n-1) + getNthFib(n-2)


# print(getNthFib(200))

# def rGCF(num1,num2):
#     if num1 == num2:
#         return num1
#     if num1 > num2:
#         return rGCF((num1-num2),num2)
#     if num2 > num1:
#         return rGCF(num1, (num2-num1))

# print(rGCF(1,75))

# def subset(str): 
#     arr=[]
#     for i in range(0, (len(str)+2)):
#         for j in range(i, len(str)+1):
#             arr.append(str[i:(j+1)])
#             print(arr)
            
#     return arr

# print(subset("abc"))

def ios(stringinput, sub = "", i = 0):
    #some code here
    if len(stringinput) == i:
        return [sub]
    else:
        return ios(stringinput, sub + stringinput[i], i+1) + ios(stringinput, sub, i+1)



print(ios("abc"))




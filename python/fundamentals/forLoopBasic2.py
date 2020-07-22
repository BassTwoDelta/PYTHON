# def BiggieSize(list):
#     for i in range(0,len(list),1):
#         if list[i] > 0:
#             list[i] = "big"
#     return list

# print(BiggieSize([-1,3,5,-5]))

# def CountP(list):
#     count = 0
#     for i in range(0,len(list),1):
#         if list[i]>0:
#             count += 1
#         list[len(list)-1] = count
#     return list

# print(CountP([-1,1,1,1]))

# def sumTotal(list):
#     sum = 0
#     for i in range(0,len(list),1):
#         sum = sum + list[i]
#     return sum

# print(sumTotal([1,2,3,4]))

# def avgList(list):
#     sum = 0
#     for i in range(0,len(list),1):
#         sum += list[i]
#     avg = sum /len(list)
#     return avg

# print(avgList([1,2,3,4]))

# def length(list):
#     return len(list)

# print(length([1,2,3,4]))

# def Minimum(list):
#     min = list[0]
#     for i in range(0,len(list),1): 
#         if list[i]< min:
#             min = list[i]
#     return min

# print(Minimum([1,3,4]))

# def Maximum(list):
#     max = list[0]
#     for i in range(0,len(list),1):
#         if list[i]>max:
#             max = list[i]
#     return max

# print(Maximum([1,3,4]))

# def UA(list):
#     D = {} 
#     min = list[0]
#     max = list[0]
#     sum = 0 
#     listLen = len(list)
#     for i in range(0,len(list),1):
#         if list[i] < min:
#             min = list[i]
#         if list[i] > max:
#             max = list[i]
#         sum += list[i]
#         avg = sum/len(list)
#     D['sumTotal'] = sum
#     D['avgerage'] = avg
#     D['minimum'] = min 
#     D['maximum'] = max
#     D['length'] = listLen
#     return D

# print(UA([37,2,1,-9]))

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# def reverseList(list): 
#     l = len(list)
#     half = int(l/2)
#     for i in range(0,len(list)-half,1):
#         temp = list[i]
#         list[i]=list[l-i-1]
#         list[l-i-1] = temp
#         print(list)
#     return list

# print(reverseList([37,2,1,-9]))
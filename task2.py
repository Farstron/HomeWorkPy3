lis = [1,2,3,4,5,6,7]
i = 0
res_lis = []
while i<len(lis)//2:
    res_lis.append(lis[i]*lis[len(lis)-1-i])
    i+=1
if len(lis)%2 == 1:
    res_lis.append(lis[i]**2)
print(res_lis)

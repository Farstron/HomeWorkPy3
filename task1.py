lis = [1,2,3,4,5,6]
i = 0
sum = 0
while i<len(lis):
    if i % 2 == 1:
        sum += lis[i]
    i+=1
print('Ответ:',sum)

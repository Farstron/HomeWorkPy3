lis = [1.1,2.2,3.001,4.4]
min = round(lis[0] - round(lis[0]),10)
max = round(lis[0] - round(lis[0]),10)
for i in lis:
    if min > round(i - round(i),10):
        min = round(i - round(i),10)
    if max < round(i - round(i),10):
        max = round(i - round(i),10)
print(max-min)

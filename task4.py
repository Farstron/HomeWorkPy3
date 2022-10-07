def to_double(num,res = 0,i = 0):
    if num!=0:
        return to_double(num//2,res+num%2*10**i,i+1)
    return res+num%2*10
num = int(input('Введите десятичное число:'))
print(to_double(num))

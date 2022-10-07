def fib(k,fib_lis=[1,0,1],pos=2):
    if k!=1:
        fib_lis.append(fib_lis[pos]+fib_lis[pos-1])
        fib_lis.reverse()
        pos+=1
        fib_lis.append(fib_lis[pos-1]-fib_lis[pos])
        fib_lis.reverse()
        return fib(k-1,fib_lis,pos+1)
    return fib_lis
k = int(input('Введите десятичное число:'))
print(fib(k))

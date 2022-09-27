def recur_factorial(n):
    if n==1:
        return n
    else:
        temp=recur_factorial(n-1)
        temp=temp * n
        return temp
print(recur_factorial(5))

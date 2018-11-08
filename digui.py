def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

def add(x,y,f):
    return f(x)+f(y)

print add(-5,6,abs)

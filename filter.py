def is_palindrome(n):
    n = str(n)
    x = 0
    if len(n) == 1:
        return True
    for y in n:
        if n[0+x] != n[-1-x]:
            return False
        x += 1
    return True
output=filter(is_palindrome,range(1,1000))
print output
print len('123')
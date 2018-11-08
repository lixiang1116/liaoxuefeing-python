def is_palindrome(n):
    n = str(n)

    for i in range(len(n)):
        if n[i]!=n[-i-1]:
            return False
    return True
output=filter(is_palindrome,range(1,1000))
print output
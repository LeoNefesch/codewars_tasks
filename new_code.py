def check_palindrome(a):
    return str(a) == str(a)[::-1]

def palindrome_chain_length(n):
    steps=0
    while(check_palindrome(n)!=True):
        n=n+int(str(n)[::-1])
        steps+=1
    return steps

if name == 'main':
    for n in range(1, 100):
        palindrome_chain_length(n)

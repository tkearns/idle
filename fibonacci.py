"what the heck is going on test 6 no branch
def fib(n):
    """ Assumes n is positive integer"""
    if n == 1 or n == 0:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n :
        result.append(a)
        temp = a
        a = b
        b = temp+b
    return result

    
def testfib(n):
    for i in range (n+1):
        print('fib of', i, ' = ',  fib(i)
    return None

def testlogicalequiv():
    # for two expressions to be logically equiv must always eval the same
    result = True
    for p in [True, False]:
        for q in [True, False]:
              result = result and (expr1(p, q) == expr1(p, q))
    print result

def expr1(p1, q1):
    result = (not p1)  or (not q1)

def expr2(p1, q1):
    return (not (p1 and q1))
              

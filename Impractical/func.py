
def f(x):
    return 5*x**2 + 3*x + 11

def fact(x):
   
    for n in range((x-1), 0, -1):
        x *= n
    return x


print(fact(6))

    
    
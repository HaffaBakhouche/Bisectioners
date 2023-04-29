from math import*

# in the case of a polynomial function, of the type mx+y
# in this case, f(x) = 32x^2+23 defined in [a;b]

def f(x):
    return 32*x*x+23    #feel free to change the function to whatever

def dichotomie(e):
    a=0
    b=2
    while b-a > e:
        m = (b+a)/2
        if f(a)*f(m)<0:
            b=m
        else:
            a=m
        print('a=',a,'b=',b)
    return (a+b)/2

e=float(input("e value: ")) #epsilon is most likely going to be a float if you deal with small numbers
print(dichotomie(e))
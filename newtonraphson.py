a=float(input("Enter value of x"))
def f(x):
    return (x**2-10)
def g(x):
    return (2*x)
for i in range(100):
    a=a-(f(a)/g(a))

print(a)


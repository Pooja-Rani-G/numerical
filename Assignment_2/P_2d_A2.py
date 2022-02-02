import numpy
from scipy import integrate

L=int(input("Enter no of itterations "))
x=numpy.linspace(0,1,L)
y=numpy.exp(x)
It=numpy.trapz(y,x)
print("Integration by Trapezoidal Method is")
print(It)
Is=integrate.simpson(y,x)
print("Integration by Simpson Method is")
print(Is)
def f(x):
	return(numpy.exp(x))

Ir=integrate.romberg(f,0,1)
print("Integration by Romberg Method is")
print(Ir)
Iq=integrate.fixed_quad(f,0,1)
print("Integration by Gaussian Quadrature Method is")
print(Iq[0])


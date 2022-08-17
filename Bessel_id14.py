
#Bessel's identity
#(14)

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

x=float(input("Enter the x: "))
n=1
theta=int(input("Enter the theta: "))
LHS=np.sin(x*np.sin(theta))
term= 2*jn(2*n-1,x)*np.sin((2*n-1)*theta)
RHS=term
s=0.0
while(abs(LHS-RHS)>1.0e-5):
    term= 2*jn(2*n-1,x)*np.sin((2*n-1)*theta)
    s=s+term
    RHS= s
    n=n+1
print("LHS: ",LHS)
print("RHS: ",RHS)

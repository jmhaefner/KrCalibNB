import numpy as np
import math
import scipy.integrate as integrate

def PfromX2(X2, dof):
	Q = ((2**(dof / 2))*math.gamma(dof/2))**(-1)
	Q = Q * integrate.quad(lambda x: (x**(dof/2-1))*math.exp(-x/2), X2, np.inf)[0]
	return Q

print('P value for X2 = 200, dof = 100:')
print(PfromX2(2, 1))

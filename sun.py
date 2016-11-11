import numpy as np

data = np.loadtxt('sun.dat')

x = data[:,0]
y = data[:,1]
z = data[:,2]
vx = data[:,3]
vy = data[:,4]
vz = data[:,5]

N = 20000
deltam = 0.1
deltae = 0.1
m_0 = 1e6
e_0 = 1.

def p(

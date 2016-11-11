import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('sismo.dat')
x = data[:,0]
y = data[:,1]
t = data[:,2]

N = 20000
deltaX = 0.1
deltaY = 0.1
X_0 = 1.
Y_0 = 1.
X = np.array([X_0])
Y = np.array([Y_0])

def p(Xe,Ye,x,y,t):
    return -0.5*np.sum((t-5./(((x-Xe)**2+(y-Ye)**2)**0.5))**2)

for i in range(1,N-1):
    UX = np.random.random()*2*deltaX-deltaX
    UY = np.random.random()*2*deltaY-deltaY
    X_new = X[-1] + UX
    Y_new = X[-1] + UY
    alpha = min(1.,np.exp(p(X_new,Y_new,x,y,t)-p(X[-1],Y[-1],x,y,t)))
    u = np.random.random()
    if(u<=alpha):
        X = np.append(X,[X_new])
        Y = np.append(Y,[Y_new])
    else:
        X = np.append(X,[X[-1]])
        Y = np.append(Y,[Y[-1]])

xe = np.median(X)
ye = np.median(Y)

print(xe,ye)

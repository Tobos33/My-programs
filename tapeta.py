import numpy as np 
import matplotlib.pyplot as plt

X = np.linspace(-2, 2, 500)
Y = X**(2/3)+(np.exp(1)/3)*(np.pi-X**3)**(1/2)*np.sin(25*np.pi*X)
Y1 = (-X)**(2/3)+(np.exp(1)/3)*(np.pi-(-X)**3)**(1/2)*np.sin(25*np.pi*(-X))
plt.plot(X, Y, color='white')
plt.plot(X, Y1, color= 'white')
plt.ylim(-2, 3)
plt.xlim(-2.5, 2.5)
plt.title("y=|x|^(2/3)+(e/3)*(pi-|x|^3)^1/2*np.sin(25*pi*|x|)")
plt.gca().set_facecolor('black') 
plt.show()
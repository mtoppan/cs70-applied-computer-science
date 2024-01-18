import numpy as np
import matplotlib.pyplot as plt                         
from mpl_toolkits.mplot3d import Axes3D

def newPlot():
    plt.figure()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()

def plot2Dline(a, b, c):
    pp = np.array([-a,c])/b
    X = np.linspace(-10,10)
    pv = np.polyval(pp,X)
    plt.plot(X,pv,'-b')
    
def plot2Dpoint(x, y):
    plt.plot(x, y, marker='o', markersize=3, color="red")   

def new3Dplot():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
def plot3Dplane(a, b, c, d):
    # break into cases to avoid division by 0
    ax = plt.gca(projection='3d')
    
    scale = 10
    granularity = 10
    x = np.linspace(-scale,scale,granularity)
    y = np.linspace(-scale,scale,granularity)

    A1,A2 = np.meshgrid(x,y)
    
    if c != 0:
        [X, Y] = [A1, A2]
        Z = (-a*X -b*Y + d)/c
    else:
        if b != 0:
            [X, Z] = [A1, A2]
            Y = (-a*X -c*Z + d)/b
        else:
            if a != 0:
                [Y, Z] = [A1, A2]
                X = (-b*Y -c*Z + d)/a
        
    ax.plot_surface(X, Y, Z, alpha = 0.5)

def plot3Dpoint(x, y, z):
    ax = plt.gca()
    ax.scatter(x, y, z, color='green')
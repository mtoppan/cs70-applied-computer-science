"""
Helper functions for Dartmouth's CS 70

Written by Wojciech Jarosz, 2020
"""

import numpy as np # for building and manipulating matrices
from matplotlib import pyplot as plt  # for graphics:

def draw_xformed_square(T=np.eye(2)):
    """
    Draw a square transformed by the 2 x 2 matrix T
    """

    # matrix with colum vectors of square vertices
    A = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T

    # transformed square vertices
    At = T @ A
    plt.plot(At[0,:], At[1,:], "-k", alpha=0.5, zorder=1)
    plt.fill(At[0,:], At[1,:], "-b", alpha=0.2)
    
    V = np.eye(2)
    Vt = T @ V

    V *= 2.5
    plt.arrow(0,0,V[0,0],V[1,0], head_width=0.1, head_length=0.1, length_includes_head=True, color='k')
    plt.arrow(0,0,V[0,1],V[1,1], head_width=0.1, head_length=0.1, length_includes_head=True, color='k')
    V *= 1.03
    plt.text(V[0,0],V[1,0], r'$x$', color='k')
    plt.text(V[0,1],V[1,1], r'$y$', color='k')
    
    plt.arrow(0,0,Vt[0,0],Vt[1,0], width=0.05, head_width=0.2, head_length=0.2, length_includes_head=True, color='r', zorder=10)
    plt.arrow(0,0,Vt[0,1],Vt[1,1], width=0.05, head_width=0.2, head_length=0.2, length_includes_head=True, color='g', zorder=10)
    
    plt.text(Vt[0,0]+0.1,Vt[1,0]+0.1, f'$({T[0,0]}, {T[1,0]})$')
    plt.text(Vt[0,1]-0.5,Vt[1,1]+0.1, f'$({T[0,1]}, {T[1,1]})$')
    
    color_lut = ['orange', 'k', 'k', 'k']
    plt.scatter(At[0,0:-1], At[1,0:-1], c=color_lut, zorder=11)
    
    plt.xticks(np.arange(-1, 4, 1))
    plt.yticks(np.arange(-1, 4, 1))
    plt.gca().set_aspect('equal')
    plt.grid()
    
def draw_xformed_shape(A,T=np.eye(2)):
    """
    Draw a shape (vertices as columns of matrix A) transformed by the 2 x 2 matrix T
    """

    # transformed square vertices
    At = T @ A
    plt.fill(At[0,:], At[1,:], "-b", alpha=0.2)
    
    V = np.eye(2)
    Vt = T @ V

    V *= 2.5
    plt.arrow(0,0,V[0,0],V[1,0], head_width=0.1, head_length=0.1, length_includes_head=True, color='k')
    plt.arrow(0,0,V[0,1],V[1,1], head_width=0.1, head_length=0.1, length_includes_head=True, color='k')
    V *= 1.03
    plt.text(V[0,0],V[1,0], r'$x$', color='k')
    plt.text(V[0,1],V[1,1], r'$y$', color='k')
    
    plt.arrow(0,0,Vt[0,0],Vt[1,0], width=0.05, head_width=0.2, head_length=0.2, length_includes_head=True, color='r', zorder=10)
    plt.arrow(0,0,Vt[0,1],Vt[1,1], width=0.05, head_width=0.2, head_length=0.2, length_includes_head=True, color='g', zorder=10)
    
    plt.text(Vt[0,0]+0.1,Vt[1,0]+0.1, f'$({T[0,0]}, {T[1,0]})$')
    plt.text(Vt[0,1]-0.5,Vt[1,1]+0.1, f'$({T[0,1]}, {T[1,1]})$')
    
    plt.scatter(At[0,:], At[1,:], zorder=11)
    
    plt.gca().set_aspect('equal')
    plt.grid()
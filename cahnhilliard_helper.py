from matplotlib import pyplot as plt
from pylab import *
import numpy as np
import random
from matplotlib.colors import LinearSegmentedColormap as lsc

###########################################################
### Any scripts necessary to run this code
###########################################################
plt.style.use('shendrukGroupStyle')		# Use our custom style and colours
import shendrukGroupFormat as ed

###########################################################
### Definitions
###########################################################
wait=0.00001
showRate=100
spread=0.1

###########################################################
### Functions
###########################################################
def niceFrame(ax,L,wait):
    plt.xlabel(r"Position, $x$")
    plt.ylabel(r"Position, $y$")
    plt.axis('off')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.set_xlim([0,L])
    ax.set_ylim([0,L])
    plt.draw()
    plt.pause(wait)

def showframe(phi,L,ax,im):
    plt.cla()
    im=imshow(phi,cmap=ed.bombpops,origin='lower',aspect="auto",vmin=-1,vmax=1)
    niceFrame(ax,L,wait)

def laplacian(f):
    """ Returns the Laplacian of a 2D array f (scalar field) """
    return roll(f,1,axis=0)+roll(f,-1,axis=0)+roll(f,1,axis=1)+roll(f,-1,axis=1)-4.0*f

def divergence(f):
    """ Returns the divergence of a 2D vector field f (2D array of vectors) """
    return 0.5*( roll(f[::,::,0],1,axis=0)-roll(f[::,::,0],-1,axis=0)+roll(f[::,::,1],1,axis=1)-roll(f[::,::,1],-1,axis=1) )

def initalizeRand(phi0,L):
    randField = spread*(2.0*np.random.rand(L,L)-1.0)
    return phi0+randField-np.mean(randField)    # Random initial condition for the phase field

def noisyField(L):
    return np.random.normal(size=(L,L,2))    # Random initial condition for the phase field

###########################################################
### Classes
###########################################################
class numericalSolver:
    # Each lattice is a square of size L
    def __init__(self,L,dt,dx,avPhi,kbt=0):
        self.L = L
        self.dt = dt
        self.dx = dx
        self.sqkbt = sqrt(2.0*kbt)                    # Thermal energy factor
        self.W2 = 1.0/(dx*dx)                         # Interface width squared
        self.phi = initalizeRand(avPhi,L)             # Phase field
        self.mu = empty(shape=(L,L),dtype=float)      # Chemical potential
        self.noise = empty(shape=(L,L,2),dtype=float) # Noise field (vector) for stochastic simulations
    def __str__(self):
        return f"Lattice: Composed of: {self.L} sites\n \tdt={self.dt}"
    def calcMu(self):
        self.mu=-( (1-self.phi*self.phi)*self.phi + self.W2*laplacian(self.phi) )
    def update(self):
        self.calcMu()
        self.noise = noisyField(self.L)
        self.phi = self.phi + self.dt * ( laplacian(self.mu)+self.sqkbt*divergence(self.noise) )  # Update the phase field
        self.phi = self.phi + self.dt * ( laplacian(self.mu) )  # Update the phase field
    def avPhi(self):
        return mean(self.phi)

from matplotlib import pyplot as plt
import argparse
from pylab import *

###########################################################
### Any scripts necessary to run this code
###########################################################
import cahnhilliard_helper as ch
plt.style.use('shendrukGroupStyle')		# Use our custom style and colours
import shendrukGroupFormat as ed

###########################################################
### User arguments
###########################################################
parser = argparse.ArgumentParser(description='Euler, central-difference d-dimensional diffusion equation solver.')
parser.add_argument("-x", "--spacestep", type=float, help="Spatial step (in simulation units of interface width).",default=1.0)
parser.add_argument("-l", "--size", type=float, help="System size (length=L; in simulation units)",default=50)
parser.add_argument("-t", "--timestep", type=float, help="Time step (in simulation units)",default=0.01)
parser.add_argument("-T", "--duration", type=float, help="Simulation time (in simulation units)",default=1000)
parser.add_argument("-kbt", "--temperature", type=float, help="Thermal energy",default=0.0)
parser.add_argument("-av", "--phi0", type=float, help="Average phase (phi0).",default=0.0)
args = parser.parse_args()

###########################################################
### Definitions
###########################################################


###########################################################
### Check input
###########################################################
print("Arguments:")
for arg, value in vars(args).items():
    print(f"\t{arg}: {value}")
T=args.duration
dt=args.timestep
dx=args.spacestep
L=int(args.size/dx)+1
phi0=args.phi0
kbt=args.temperature

###########################################################
### Initialize the system
###########################################################
solver=ch.numericalSolver(L,dt,dx,phi0,kbt)
fig,ax = plt.subplots(nrows=1, ncols=1) # Setup figure for animation
im=imshow(solver.phi,cmap=ed.bombpops,origin='lower',aspect="auto",vmin=-1,vmax=1)
cbar=plt.colorbar(im)
cbar.set_label(r'Phase, $\phi$')

###########################################################
### Simulate
###########################################################
for t in range(1,int(T/dt)+1):
    solver.update()
    if(t%ch.showRate==0):
        ch.showframe(solver.phi,L,ax,im)
        print(solver.avPhi(),phi0)

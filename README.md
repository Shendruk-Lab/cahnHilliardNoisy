# Cahn-Hilliard Equation Solver
**Euler, central-difference (applied twice sequentially) 2D Cahn-Hilliard equation solver.**
**Euler–Maruyama method for the noise.**

Python scripts for numerically solving the Cahn-Hilliard equation in 2-dimensions with noise. 
The noisy Cahn-Hilliard equation is
$$\partial_t \phi = M\nabla^2 \mu + \sqrt{ 2k_\text{B}T M } \nabla\cdot\eta , $$
where the chemical potential is $\mu = a\phi(\phi^2-1) - k\nabla^2\phi$. 
Non-dimensionalized in space by interface width $\sqrt{k/a}$ and time by $k/(M a^2)$. 
This means mobility $M=1$, surface tension $k=1$ and bulk free energy $a=1$ are set to unity. 
Initialized randomly. 

## diffEq_helper.py
This script has all the functions and classes in it for running the simulations. 

## diffEq.py
This script numerically solves the diffusion equation and makes a movie of it. 
### Arguments:
- `l`, `size`, System size. Integer. Default=100
- `t`, `timestep`, Time step. Float. Default=0.01
- `T`, `duration`, Simulation duration or total time (in simulation units). Float. Default=1000.0
- `x`, `spacestep`, Spatial step (in sim units of characteristic interface width). Float. Default=1.0
- `kbt`, `temperature`, Thermal energy (in sim units). Float. Default=0
- `a`, `avPhi`, Average phase (phi). Float. Default=0.0

### Ouput:
- None
### Requirements:
- `cahnhilliard_helper.py`
### Command line example:
```
python3 cahnhilliard.py -T 10000 -l 100 -av 0.0 -t 0.002 -x 1  -kbt 0.1
```

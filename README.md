# Cahn-Hilliard Equation Solver
**Euler, central-difference (applied twice sequentially) 2D Cahn-Hilliard equation solver.**

Python scripts for numerically solving the cahn-hilliard equation in 2-dimensions. 
Non-dimensionalized in space by spatial step size and time by mobility*freeEn/(step size)^2. 
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
- `a`, `avPhi`, Average phase (phi). Float. Default=0.0

### Ouput:
- None
### Requirements:
- `cahnhilliard_helper.py`
### Command line example:
```
python3 cahnhilliard.py -l 100 -t 0.01 -T 10000 -a 0.0 -w 2.0
```

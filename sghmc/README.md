### Installation

Run code below in commend line for installation:
```
$ git clone https://github.com/kingcheng12/Stochastic-Gradient-HMC-with-Friction.git
$ cd cd Stochastic-Gradient-HMC-with-Friction/sghmc/
$ python setup.py install
```

### Description

The package contains function SGHMC and SGHMC_parallel. 

Run code below in python environment for function instruction:

```
from sghmc.module import SGHMC, SGHMC_parallel
SGHMC?
SGHMC_parallel?
```

### Instruction for SGHMC_parallel

Run code below in commend line to set up cores before applying SGHMC_parallel

```
ipcluster start -n 4
```

You may change 4 to other specific number of engines.
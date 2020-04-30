### Installation

Run code below in commend line for installation:
```
$ pip install --index-url https://test.pypi.org/simple/ SGHMC-GOZH
```

Then import functions in python environment with code below:
```
from sghmc.module import SGHMC, SGHMC_parallel
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
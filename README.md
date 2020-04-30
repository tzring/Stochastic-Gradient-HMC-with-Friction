# SGHMC with Friction

Implementation of Stochastic Gradient Hamiltonian Monte Carlo.

The original paper is available on http://proceedings.mlr.press/v32/cheni14.pdf.

This is the final project for STA 663 of Duke University. It is contributed by Zhenyu Tian (zhenyu.tian@duke.edu) and Gongjinghao Cheng (gongjinghao.cheng@duke.edu)

### Repository structure

- `sghmc/` : package containing modules

- `Report/` : project report

- `example/` : examples for development and module testing

- `development log/` : development history

### Installation

Run following code on commend for package installation:

```
$ pip install --index-url https://test.pypi.org/simple/ SGHMC-GOZH
```

Then import functions in python environment with code below:
```
from sghmc.module import SGHMC, SGHMC_parallel
```

Refer to project report for further details.

import setuptools

setuptools.setup(
    name="sghmc",
    version="0.0.1",
    author="Zhenyu Tian, Gongjinghao Cheng",
    author_email="zhenyu.tian@duke.edu, gongjinghao.cheng@duke.edu",
    description="realization of Stochastic Gradient Hamiltonian Monte Carlo",
    url="https://github.com/kingcheng12/Stochastic-Gradient-HMC-with-Friction",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License ::  OSI Approved:: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "matplotlib >= 3.1.1",
        "numpy >= 1.17.2",
        "numba >= 0.45.1",
        "seaborn >= 0.9.0",
        "scipy >= 1.4.1",
        "ipyparallel >= 6.2.5"
    ],
)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SGHMC_GOZH", # Replace with your own username
    version="0.0.1",
    author="Zhenyu Tian, Gongjinghao Cheng",
    author_email="zhenyu.tian@duke.edu, gongjinghao.cheng@duke.edu",
    description="realization of Stochastic Gradient Hamiltonian Monte Carlo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kingcheng12/Stochastic-Gradient-HMC-with-Friction",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

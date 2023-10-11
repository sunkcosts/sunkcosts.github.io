# Setup

## Model

## Reproduce

Install miniconda

```bash
brew install --cask miniconda
```

create environment

```bash
conda create -n sunkcosts python=3.11 -y
conda activate sunkcosts
```

install package

```bash
pip install sunklib
```

```shell title="Install & Run Model Locally"
pip install sunklib # install package from pypi
sunklib initialize # initialize package
scli run model --open # run model and open in browser
```



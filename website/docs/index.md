# Docs

For the purpose of reproducibility, the [code](https://github.com/sunkcosts) used for the analysis is open source.

<!-- You can submit a GitHub issue in the relevant repository if you find any inaccuracies. -->

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


## Package structure

- main package and docs: repo > sunkcosts.github.io
- artifacts: repo > artifacts
- streamlit share app: repo > sunkcosts.model
    - includes artifacts necessary to run app
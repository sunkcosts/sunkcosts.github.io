# Sunk Costs

Description

## Reproducibility

## Setup

We cover the steps to setup and run the various scripts and notebooks below.

### Install Miniconda

It is optional but recommended you install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) for environment management.

```bash
# install miniconda with homebrew
brew install --cask miniconda
```

### Clone Repository

Clone the repository into the directory you would like to operate in.

```bash
# if ssh key configured
git clone git@github.com:sunkcosts/sunkcosts.github.io.git
# enter directory
cd sunkcosts
```

```bash
# if no ssh key configured
git clone https://github.com/sunkcosts/sunkcosts.github.io.git
# enter directory
cd sunkcosts
```

### Create Environment & Install Dependencies

Create conda environment, activate it, and install the requirements.

```bash
conda create -n sunkcosts python=3.11 -y
conda activate sunkcosts
pip install poetry
poetry install
```

### Obtain Mapbox API Key

[Mapbox] is a service... TODO You will need to install obtain a free API key from them in order to run some of the scripts, specifically for the collection of geolocation and terrain data.




## Running Scripts



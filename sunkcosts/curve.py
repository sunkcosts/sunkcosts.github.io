import numpy as np

from numpy.polynomial import Polynomial
from scipy.optimize import curve_fit
from scipy.stats import norm, beta, skewnorm


class SkewedNormalDist:
    def __init__(self) -> None:
        self.__function = None

    def fit(self, distribution):
        self.a, self.loc, self.scale = skewnorm.fit(distribution)
        self.__function = lambda x: skewnorm.pdf(
            x, a=self.a, loc=self.loc, scale=self.scale
        )

    def predict(self, x):
        assert self.__function is not None
        return self.__function(x)


class PolynomialFunction:
    def __init__(self, deg: int) -> None:
        self.__deg = deg
        self.__function = None

    def fit(self, X, Y):
        self.__function = Polynomial.fit(X, Y, deg=self.__deg)

    def predict(self, x) -> float:
        assert self.__function is not None
        return self.__function(x)


class ExponentialFunction:
    # https://stackoverflow.com/questions/21420792/exponential-curve-fitting-in-scipy
    def __init__(self, p0=(1, 1e-6, 1), maxfev=10_000) -> None:
        self.p0 = p0
        self.params = None
        self.maxfev = maxfev  # maximum number of calls to fit data

    def exponential(self, x, a, c, d):
        return a * np.exp(-c * x) + d

    def fit(self, X, Y):
        self.params, _ = curve_fit(self.exponential, X, Y, p0=self.p0, maxfev=self.maxfev)

    def predict(self, x):
        assert self.params is not None
        return self.exponential(x, *self.params)

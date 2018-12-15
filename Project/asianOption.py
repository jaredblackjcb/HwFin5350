import abc
import enum
import numpy as np
from scipy.stats import binom
from scipy.stats import norm
from scipy.stats.mstats import gmean

import numpy as np
from scipy.stats import norm


def blackScholesCall(spot, strike, rate, vol, div, expiry):
    d1 = (np.log(spot / strike) + (rate - div + 0.5 * vol * vol) * expiry) / (vol * np.sqrt(expiry))
    d2 = d1 - vol * np.sqrt(expiry)
    callPrice = (spot * np.exp(-div * expiry) * norm.cdf(d1)) - (strike * np.exp(-rate * expiry)  * norm.cdf(d2))
    return callPrice

def geometricAsianCall(spot, strike, rate, vol, div, expiry, N):
    dt = expiry / N
    nu = rate - div - 0.5 * vol * vol
    a = N * (N+1) * (2.0 * N + 1.0) / 6.0
    V = np.exp(-rate * expiry) * spot * np.exp(((N + 1.0) * nu / 2.0 + vol * vol * a / (2.0 * N * N)) * dt)
    vavg = vol * np.sqrt(a) / pow(N, 1.5)
    callPrice = blackScholesCall(V, strike, rate, vavg, div, expiry)
    return callPrice

def AssetPaths(spot, mu, sigma, expiry, div, nreps, nsteps):
    paths = np.empty((nreps, nsteps + 1))
    h = expiry / nsteps
    paths[:, 0] = spot
    mudt = (mu - div - 0.5 * sigma * sigma) * h
    sigmadt = sigma * np.sqrt(h)

    for t in range(1, nsteps + 1):
        z = np.random.normal(size=nreps)
        paths[:, t] = paths[:, t - 1] * np.exp(mudt + sigmadt * z)

    return paths
# compute a price path with 10 time steps and store each price in an array
K = 100
T = 1
S = 100
sig = 0.2
r = 0.06
div = 0.03
N = 10
M = 10000
t = np.zeros(10)

######## Compute the control variate portfolio value #################3
# precompute constants
nreps = M
nsteps = N
expiry = T
dt = expiry / nsteps
nudt = (r - div - 0.5 * sig ** 2) * dt
sigsdt = sig * np.sqrt(dt)
t = np.zeros(nsteps)
# lnS = np.log(S)

sum_CT = 0
sum_CT2 = 0
global paths
paths = AssetPaths(S, r, sig, expiry, div, nreps, nsteps)

# repeat M times
for j in range(nreps):

    # calculate arithmetic and geometric means for each path
    A = np.mean(paths[j])
    G = gmean(paths[j])

    # get payoff
    CT = max(0, A - K) - max(0, G - K)
    sum_CT += CT
    sum_CT2 += CT * CT

portfolio_value = sum_CT / nreps * np.exp(-r * expiry)
SD = np.sqrt((sum_CT2 - sum_CT * sum_CT / nreps) * np.exp(-2 * r * expiry) / (nreps - 1))
SE = SD / np.sqrt(nreps)
callPrice = portfolio_value + geometricAsianCall(S, K, r, sig, div, expiry, nsteps)
print(portfolio_value, callPrice)
print(sum_CT)
print(A,G)
print(expiry)


import numpy as np

# compute a price path with 10 time steps and store each price in an array
K = 100
T = 1
S = 100
sig = 0.2
r = 0.06
div = 0.03
M = 2
nsteps = 10


#def AssetPaths(K, T, S, sig, r, div, M, nsteps ):
paths = np.empty((M, nsteps + 1))
# precompute constants
dt = T / nsteps
nudt = (r - div - 0.5 * sig ** 2) * dt
sigsdt = sig * np.sqrt(dt)

paths[:, 0] = S
v = r - div - .5 * sig ** 2
# compute a price path with 10 steps
for t in range(1, nsteps +1):
    z = np.random.normal(size=M)  # use engine.replications in probo
    paths[:, t] = paths[:, t-1] * np.exp(nudt + sigsdt * z)
    avg = np.mean(paths[t])
    return maximum(avg - option.strike, 0.0)
#avgpaths = np.mean(paths)
#print(avgpaths)
#print(paths)
#print(np.mean(paths[0]))
#print(np.mean(paths[1]))

###################################################################################################Class
# Use NaiveMonteCarloPricer(engine, option, data):   #In a blacksholes world, only takes into account ending prices
# The next function Pathwisemontecarlo takes into account paths
#from stop-loss.py import AssetPaths
# inside pathwisenaivemontecarlopricer

    #############ControlVariate###################
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
    dt = T / N
    nudt = (r - div - 0.5 * sig ** 2) * dt
    sigsdt = sig * np.sqrt(dt)
    # lnS = np.log(S)

    sum_CT = 0
    sum_CT2 = 0

    # repeat M times
    for j in range(M):
        St = S
        sumSt = 0
        productSt = 1

        for i in range(N):
            e = np.random.randn(1)
            St = St * np.exp(nudt + sigsdt * e)
            sumSt += St
            productSt *= St

        A = sumSt / N
        G = productSt ** (1 / N)
        CT = max(0, A - K) - max(0, G - K)
        sum_CT += CT
        sum_CT2 += CT * CT

    porfolio_value = sum_CT / M + np.exp(-r * T)
    SD = np.sqrt((sum_CT2 - sum_CT * sum_CT / M) * np.exp(-2 * r * T) / (M - 1))
    SE = SD / np.sqrt(M)

    ################################################################################




    # paste paths = AssetPaths(spot, mu, sigma, expiery, div, nreps, nsteps):
    (spot, rate, vol, div) = data.get_data()
    expiry = option.expiry
    nreps = engine.replications
    nsteps = engine.time_steps
    paths = AssetPaths(spot, mu, sigma, expiry, div, nreps, nsteps)
    call_t = 0.0
        #the parameters come from engine, option, and data

    for i in range(nreps):
        call_t += option.payoff(paths[i])

    call_t /= nreps
    call_t *= np.exp(-r * expiry)
    #add a line that adds standard error
    return (call_t, stderr)


# go to McDonald ch.19 ex.19.2 to check and see if calculations are pretty close to the same value
# the controlvariate pricer is the only pricer we need to turn in
# the pathwisemontecarlopricer is an intermediate step and we can add
### Number 4

from scipy.stats import binom
import numpy as np

##Call Payoff function
def callPayoff(spot, strike):
    return np.maximum(spot - strike, 0.0)


##Put payoff function
def putPayoff(spot, strike):
    return np.maximum(strike - spot, 0.0)

## Multiperiod binomial pricer
def binomialPricer(S, K, r, v, q, T, n, payoff, verbose = True):
    nodes = n  + 1
    h = T / n
    u = np.exp((r - q) * h + v * np.sqrt(h))
    d = np.exp((r - q) * h - v * np.sqrt(h))
    pstar = (np.exp((r - q) * h) - d) / (u - d)
    
    price = 0.0
    
    for i in range(nodes):
        prob = binom.pmf(i, n, pstar)
        spotT = S * (u ** i) * (d ** (n - i))
        po = payoff(spotT, K) 
        price += po * prob
        if verbose:
            print(f"({spotT:0.4f}, {po:0.4f}, {prob:0.4f})")
        
    price *= np.exp(-r * T)
    
    print(price)
    

S = 80.0
K = 95.0
r = 0.08
v = 0.30
q = 0.0
T = 1
n = 3
h = T / n
u = 1.3 # np.exp((r - q) * h + v * np.sqrt(h))
d = 0.8 #np.exp((r - q) * h - v * np.sqrt(h))
pstar = (np.exp((r - q) * h) - d) / (u - d) 

nodes = n + 1
spotT = np.zeros((nodes, ))


print("Call option price at S=80: ")
price80 = binomialPricer(S, K, r, v, q, T, n, callPayoff, verbose = False)







S = 90.0
K = 95.0
r = 0.08
v = 0.30
q = 0.0
T = 1
n = 3
h = T / n
u = 1.3 # np.exp((r - q) * h + v * np.sqrt(h))
d = 0.8 #np.exp((r - q) * h - v * np.sqrt(h))
pstar = (np.exp((r - q) * h) - d) / (u - d) 

nodes = n + 1
spotT = np.zeros((nodes, ))

print("Call option price at S=90: ")
price90 = binomialPricer(S, K, r, v, q, T, n, callPayoff, verbose = False)





S = 110.0
K = 95.0
r = 0.08
v = 0.30
q = 0.0
T = 1
n = 3
h = T / n
u = 1.3 # np.exp((r - q) * h + v * np.sqrt(h))
d = 0.8 #np.exp((r - q) * h - v * np.sqrt(h))
pstar = (np.exp((r - q) * h) - d) / (u - d) 

nodes = n + 1
spotT = np.zeros((nodes, ))
print("Call option price at S=110:")
price110 = binomialPricer(S, K, r, v, q, T, n, callPayoff, verbose = False)






S = 120.0
K = 95.0
r = 0.08
v = 0.30
q = 0.0
T = 1
n = 3
h = T / n
u = 1.3 # np.exp((r - q) * h + v * np.sqrt(h))
d = 0.8 #np.exp((r - q) * h - v * np.sqrt(h))
pstar = (np.exp((r - q) * h) - d) / (u - d) 

nodes = n + 1
spotT = np.zeros((nodes, ))
print("Call option price at S=120:")
price120 = binomialPricer(S, K, r, v, q, T, n, callPayoff, verbose = False)





S = 130.0
K = 95.0
r = 0.08
v = 0.30
q = 0.0
T = 1
n = 3
h = T / n
u = 1.3 # np.exp((r - q) * h + v * np.sqrt(h))
d = 0.8 #np.exp((r - q) * h - v * np.sqrt(h))
pstar = (np.exp((r - q) * h) - d) / (u - d) 

nodes = n + 1
spotT = np.zeros((nodes, ))
print("Call option price at S=130:")
price130 = binomialPricer(S, K, r, v, q, T, n, callPayoff, verbose = False)


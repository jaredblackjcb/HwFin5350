# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:31:09 2018

@author: jcbla
"""


import numpy as np
from scipy.stats import binom

S = 100
K = 95
r = .08
v = .3
q = 0
T = 1
n = 3

##Call Payoff function
def callPayoff(spot, strike):
    return np.maximum(spot - strike, 0.0)


##Put payoff function
def putPayoff(spot, strike):
    return np.maximum(strike - spot, 0.0)



### The Full Recursive solution for the European Binomial Model

def euroBinomPricerRecursive(S, K, r, v, q, T, n, payoff, verbose = True):
    nodes = n  + 1
    h = T / n
    u = np.exp((r - q) * h + v * np.sqrt(h))
    d = np.exp((r - q) * h - v * np.sqrt(h))
    pu = (np.exp((r - q) * h) - d) / (u - d)
    pd = 1.0 - pu
    disc = np.exp(-r * h)
    
    
    ## Arrays to store the spot prices and option values
    Ct = np.empty(nodes)
    St = np.empty(nodes)
    
    for i in range(nodes):
        St[i] = S * (u ** (n - i)) * (d ** i)
        Ct[i] = payoff(St[i], K)
    
    if verbose:
        print(Ct)
        
    for t in range((n - 1), -1, -1):
        for j in range(t+1):
            Ct[j] = disc * (pu * Ct[j] + pd * Ct[j+1])
            # St[j] = St[j] / u
            # Ct[j] = np.maximum(Ct[j], early payoff)
            #print(Ct)
            
    return Ct[0]
            


callPrc = euroBinomPricerRecursive(S, K, r, v, q, T, n, callPayoff, verbose=False)
print(f"The European Call Premium: ${callPrc : 0.3f}")

putPrc = euroBinomPricerRecursive(S, K, r, v, q, T, n, putPayoff, verbose=False)
print(f"The European Put Premium: ${putPrc : 0.3f}")

def americanBinomPutPricerRecursive(S, K, r, v, q, T, n, verbose = True):
    nodes = n  + 1
    h = T / n
    u = np.exp((r - q) * h + v * np.sqrt(h))
    d = np.exp((r - q) * h - v * np.sqrt(h))
    pu = (np.exp((r - q) * h) - d) / (u - d)
    pd = 1.0 - pu
    disc = np.exp(-r * h)
    
    
    ## Arrays to store the spot prices and option values
    Ct = np.empty(nodes)
    St = np.empty(nodes)
    
    for i in range(nodes):
        St[i] = S * (u ** (n - i)) * (d ** i)
        Ct[i] = putPayoff(St[i], K)
    
    if verbose:
        print(Ct)
        
    for t in range((n - 1), -1, -1):
        for j in range(t+1):
            Ct[j] = disc * (pu * Ct[j] + pd * Ct[j+1])
            St[j] = St[j] / u
            Ct[j] = np.maximum(Ct[j], K - St[j])
            #print(Ct)
            
    return Ct[0]

def americanBinomCallPricerRecursive(S, K, r, v, q, T, n, verbose = True):
    nodes = n  + 1
    h = T / n
    u = np.exp((r - q) * h + v * np.sqrt(h))
    d = np.exp((r - q) * h - v * np.sqrt(h))
    pu = (np.exp((r - q) * h) - d) / (u - d)
    pd = 1.0 - pu
    disc = np.exp(-r * h)
    
    
    ## Arrays to store the spot prices and option values
    Ct = np.empty(nodes)
    St = np.empty(nodes)
    
    for i in range(nodes):
        St[i] = S * (u ** (n - i)) * (d ** i)
        Ct[i] = callPayoff(St[i], K)
    
    if verbose:
        print(Ct)
        
    for t in range((n - 1), -1, -1):
        for j in range(t+1):
            Ct[j] = disc * (pu * Ct[j] + pd * Ct[j+1])
            St[j] = St[j] / u
            Ct[j] = np.maximum(Ct[j], St[j] - K)
            #print(Ct)
            
    return Ct[0]
callPrc = americanBinomCallPricerRecursive(S, K, r, v, q, T, n, verbose=False)
print(f"The American Call Premium: ${callPrc : 0.3f}")

putPrc = americanBinomPutPricerRecursive(S, K, r, v, q, T, n, verbose=False)
print(f"The American Put Premium: ${putPrc : 0.3f}")

print("The call prices for the American and European options are the same because the stock pays no dividend. \nThat means there is no early exercise.")
print("The put-call parity does not hold because the American and European options have the same call price and different put prices.")


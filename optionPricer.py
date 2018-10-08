import numpy as np
import math

# Declare variables
S = [80.0, 90.0, 110.0, 120.0]
K = 95.0
r = .08
T = 1.0
n = 3.0
u = 1.3
d = 0.8

for i in range(len(S)):
    spotPrice = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]
    spotPrice[0][0] = S[i]
    spotPrice[1][0] = S[i] * u
    spotPrice[1][1] = S[i] * d
    spotPrice[2][0] = S[i] * u ** 2
    spotPrice[2][1] = S[i] * u * d
    spotPrice[2][2] = S[i] * d ** 2
    spotPrice[3][0] = S[i] * u ** 3
    spotPrice[3][1] = S[i] * u ** 2 * d
    spotPrice[3][2] = S[i] * d ** 2 * u
    spotPrice[3][3] = S[i] * d ** 3

    payoff = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]
    payoff[0][0] = spotPrice[0][0] - K if spotPrice[0][0] > K else 0
    payoff[1][0] = spotPrice[1][0] - K if spotPrice[1][0] > K else 0
    payoff[1][1] = spotPrice[1][1] - K if spotPrice[1][1] > K else 0
    payoff[2][0] = spotPrice[2][0] - K if spotPrice[2][0] > K else 0
    payoff[2][1] = spotPrice[2][1] - K if spotPrice[2][1] > K else 0
    payoff[2][2] = spotPrice[2][2] - K if spotPrice[2][2] > K else 0
    payoff[3][0] = spotPrice[3][0] - K if spotPrice[3][0] > K else 0
    payoff[3][1] = spotPrice[3][1] - K if spotPrice[3][1] > K else 0
    payoff[3][2] = spotPrice[3][2] - K if spotPrice[3][2] > K else 0
    payoff[3][3] = spotPrice[3][3] - K if spotPrice[3][3] > K else 0

    delta = [[0], [0, 0], [0, 0, 0]]
    delta[2][0] = (payoff[3][0] - payoff[3][1]) / (spotPrice[2][0] * (u - d))
    delta[2][1] = (payoff[3][1] - payoff[3][2]) / (spotPrice[2][1] * (u - d))
    delta[2][2] = (payoff[3][2] - payoff[3][3]) / (spotPrice[2][2] * (u - d))
    delta[1][0] = (payoff[2][0] - payoff[2][1]) / (spotPrice[1][0] * (u - d))
    delta[1][1] = (payoff[2][1] - payoff[2][2]) / (spotPrice[1][1] * (u - d))
    delta[0][0] = (payoff[1][0] - payoff[1][1]) / (spotPrice[0][0] * (u - d))
    print("Delta for spot price ", S[i], ": \n", delta)

    B = [[0], [0, 0], [0, 0, 0]]
    B[2][0] = math.exp(-r * (T / n)) * ((u * payoff[3][0] - d * payoff[3][1]) / (u - d))
    B[2][1] = math.exp(-r * (T / n)) * ((u * payoff[3][1] - d * payoff[3][2]) / (u - d))
    B[2][2] = math.exp(-r * (T / n)) * ((u * payoff[3][2] - d * payoff[3][3]) / (u - d))
    B[1][0] = math.exp(-r * (T / n)) * ((u * payoff[2][0] - d * payoff[2][1]) / (u - d))
    B[1][1] = math.exp(-r * (T / n)) * ((u * payoff[2][1] - d * payoff[2][2]) / (u - d))
    B[0][0] = math.exp(-r * (T / n)) * ((u * payoff[1][0] - d * payoff[1][1]) / (u - d))
    print("B for spot price ", S[i], ":\n", B)

    premium = [[0], [0, 0], [0, 0, 0]]
    premium[2][0] = delta[2][0] * spotPrice[2][0] + B[2][0]
    premium[2][1] = delta[2][1] * spotPrice[2][1] + B[2][1]
    premium[2][2] = delta[2][2] * spotPrice[2][2] + B[2][2]
    premium[1][0] = delta[1][0] * spotPrice[1][0] + B[1][0]
    premium[1][1] = delta[1][1] * spotPrice[1][1] + B[1][1]
    premium[0][0] = delta[0][0] * spotPrice[0][0] + B[0][0]
    print("Call option premiums for spot price ", S[i], ":\n", premium)
    
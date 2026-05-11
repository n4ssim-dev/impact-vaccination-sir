# Import des dépendences du projet
# numpy : exploration de données (chiffres)
# matplotlib : visualisation de données (graphs)
import numpy as np
import matplotlib.pyplot as plt

# Population initial
N = 10000
# Infectés initial
I0 = 10
# proportion de vaccinées
pv = 0.20
# Taux de transmission
transmission = 0.3
# Taux de retrait
retrait = 0.1
# Jours de la simulation
jours = 100
# Susceptibles initial
S0 = (1 - pv)* N
# Nombre initial de vaccinés
R0 = pv * N

'''
    𝑆0=(1−𝑝𝑣)⋅𝑁
    𝑅0=𝑝𝑣⋅𝑁

    𝑆0 = nombre initial de personnes susceptibles, 
    𝑅0 = nombre initial de personnes vaccinées (donc immunisées), 
    𝑝𝑣 = proportion de vaccinés, 
    𝑁 = population totale.
'''

def simulate_sir(S0, I0, R0, transmission, retrait, jours):
    S = [S0]
    I = [I0]
    R = [R0]
    for t in range(0, jours):
        # TODO : calculer dS
        dS = I 
        # TODO : calculer dI
        dI = transmission * float(I[t]) * (S[t] / N)
        # TODO : calculer dR
        dR = retrait * float(I[t])
        # TODO : mettre à jour S, I, R
        S.append(S[t] - dI)
        I.append(I[t] + dI - dR)
        R.append(R[t] + dR)
    return np.array(S), np.array(I), np.array(R)
  
#Dictionnaire
scenarios = {
    "0% vaccinés": 0.0,
    "30% vaccinés": 0.3,
    "60% vaccinés": 0.6
}
plt.figure(figsize=(10, 6))
for label, pv in scenarios.items():
    # TODO : calculer S0 et R0
    S0 = (1- pv) * N
    R0 = pv * N
    # TODO : lancer la simulation
    S, I, R = simulate_sir(S0, I0, R0, transmission, retrait, jours)
    # TODO : tracer I(t)
    plt.plot(I, label=label)
plt.title("Evolution du nombres d'infectes")
plt.xlabel("Jour")
plt.ylabel("Nombre d'infectés")
plt.legend()
plt.grid(True)
plt.savefig('testplot.png')
plt.close()
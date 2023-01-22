pop = [1,2,3,4,5,6,7,8,9,10]
fitness = [1,2,3,4,5,6,7,8,9,10]

somme = sum(fitness)
proba = [fit/somme for fit in fitness]

import random
from tqdm import tqdm

nb_chiffre = [0 for _ in range(10)]

loop = int(1e6)

for _ in tqdm(range(loop)):
    newChiffre = random.choices(pop,proba,k=1)
    nb_chiffre[newChiffre[0]-1] += 1

for i, count in enumerate(nb_chiffre):
    print(f"{i+1}) {count}    rendement :  {round((count/(loop*proba[i]))*100)}%    with    {round(proba[i]*100)}%")
'''
Script to create random Data to use in Model
'''

#zero for -ve and one for +ve
#in case diffBreath(difficulty breathing) column, minus one is for high -ve, 0 for low -ve and one for +ve

import random
import pandas as pd
import numpy as np

index = np.arange(100)
randomValueList=[]
for i in range(2500):
	randomValue='{:04.3f}'.format(random.uniform(93, 104))
	randomValueList.append(randomValue)

fever = np.array(randomValueList)
#fever = np.random.randint(92.0,104.0,size=2500)
bodyPain  = np.random.randint(2,size=2500)
age  = np.random.randint(20,80,size=2500)
runnyNose  = np.random.randint(2,size=2500)
diffBreath  = np.random.randint(-1,2,size=2500)
infectionProb  = np.random.randint(2,size=2500)

data = {'fever':fever,'bodyPain':bodyPain,'age':age,'runnyNose':runnyNose,'diffBreath':diffBreath,'infectionProb':infectionProb}
df = pd.DataFrame(data)
df.to_csv('data.csv',index=False)
import numpy as np
import pandas as pd

populationData = pd.read_json('https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population.json')
stringDataFrame = pd.DataFrame(pd.np.empty(0,1))
for index, row in populationData.iterrows():
    stringDataFrame.append(pd.Series(row[0] + ' has population ' + str(row[1])))

i=0
while i < 10**8:
    i+=1

print('The code is done!')

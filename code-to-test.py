import pandas as pd

populationData = pd.read_json('https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population.json')

for dataPoint in populationData:
  print(dataPoint['country'] + ' has population ' + dataPoint[''])

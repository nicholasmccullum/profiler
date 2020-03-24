import pandas as pd

populationData = pd.read_json('https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population.json')

for index, row in populationData.iterrows():
    print(row[0] + ' has population ' + str(row[1]))

import json as js
import pandas as pd
with open("/home/tdpro/format-converter/aiml/database/animal.json", 'r') as f:
        data =  js.loads(f.read())

df = pd.DataFrame(data,columns = ["name","indentify","eat","location"]) #example df = pd.DataFrame(data,columns = ["name","indentify","eat","location"])
df.to_csv ("/home/tdpro/format-converter/aiml/save/datacsv/animal.csv", index = False)
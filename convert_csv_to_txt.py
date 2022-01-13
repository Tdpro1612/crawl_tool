import pandas as pd
df = pd.read_csv(path_file)

data = df[['name','indentify']]


data.to_csv("animal_indentify.txt",sep=":",columns=None,header=False,index=False)
import json
import os
import pandas as pd 
def to_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        
def to_excel(data, path):
    df= pd.DataFrame([data])
    df.to_excel(path, index=False)
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
df= pd.read_excel("/Users/blair/budget_db.xlsx")
df.set_index("item", drop=True, inplace=True)
db_dict = df.to_dict(orient="index")

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client["budget"]     
db.cost.insert_one(db_dict)       



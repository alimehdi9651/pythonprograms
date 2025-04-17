import pandas as pd 
# pf = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# pf = pd.read_excel("SampleSuperstore.xlsx")

pf = pd.read_json("sample_Data.json")
print(pf)
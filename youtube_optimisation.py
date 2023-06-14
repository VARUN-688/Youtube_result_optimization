import data_preprocess
import decision_tree
import model
import pandas as pd
import numpy as np

df = pd.read_csv("youtube_data.csv")
df=data_preprocess.get_dataFrame(df)
print(df)

decision_tree.get_frame(df)
test_data=pd.read_csv("test_data.csv")
test_data=data_preprocess.get_dataFrame(test_data)
result=test_data.apply(model.id3,axis="columns")
print(result.loc[:,['Play','Subs_groups','Views_groups']])

# 2.List-to-Series conversion with Custom Indexing.
import pandas as pd
a=[2,4,5,6,9]
s=pd.Series(a,index=[1,3,5,7,9])
print(s)
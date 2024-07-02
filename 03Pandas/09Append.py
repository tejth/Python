import pandas as pd

var1= pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]},index=["a","b","c","d"])
var2 = pd.DataFrame({"C":[10,20],"D":[11,22]}, index=["a","b"])

# var1.append(var2)
var1.append(var2,ignore_index=True)



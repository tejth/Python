import pandas as pd;


#Melt
var = pd.DataFrame({"days":[1,2,3,4,5,6],"eng":[10,12,14,15,16,12],"maths":[17,18,13,14,16]})
print(var)
print()
print()


pd.melt(var)
# pd.melt(var,id_vars=["days"],var_name="python")


#Pivot
var1 = pd.DataFrame({"days":[1,2,3,4,5,6],"st_name":["a","b","c","a","b","c"],"eng":[10,12,14,15,16,12],"maths":[17,18,13,14,16]})
# var1.pivot(index="days",columns="st_name")
# var1.pivot(index="days",columns="st_name",values="eng")
var1.pivot_table(index="days",columns="st_name",aggfunc="mean")



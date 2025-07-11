import pandas as pd
# myseries = [1,2,3,4,5,2,3,4,3,3]
# myvar = pd.Series(myseries)
# print(myvar)

#labeling the series with use of the index parameter
a = [1,4,2]
myvar = pd.Series(a, index = ["x", "y","z"])
print(myvar)

# accesing the element through the labels
print(myvar["z"])#this returns the value respective to the lable z which is 2
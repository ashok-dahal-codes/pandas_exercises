import pandas as pd
calories = {
    "day-1":30,
    "day-2":90,
    "day-3":12,
}
myvar = pd.Series(calories)
print(myvar)
print(myvar["day-2"])

myvar2 = pd.Series(calories, index = ["day-2", "day-3"])
print(myvar2)
print(myvar2["day-3"])
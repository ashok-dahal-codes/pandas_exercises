import pandas as pd

mycar = {
    "brand":["totyota", "bmw", "mercedes-benz"],
    "passings":[1,3,7]
    }
myval = pd.DataFrame(mycar)
print(myval)
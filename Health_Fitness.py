import argparse
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description="Health checkup")
parser.add_argument("--name", required=True)
parser.add_argument("--blood", required=True)
parser.add_argument("--Age", type=int, required=True)
parser.add_argument("--Blood_pressure", type=int, required=True)
parser.add_argument("--Sugar", type=int, required=True)

argums = parser.parse_args()

data = {
    "Patient Name": [argums.name],
    "Age": [argums.Age],
    "Blood Group": [argums.blood],
    "Blood Pressure": [argums.Blood_pressure],
    "Sugar Level": [argums.Sugar]
}

df = pd.DataFrame(data)

bp_array = np.array(df["Blood Pressure"])
sugar_array = np.array(df["Sugar Level"])

print("Health Report:", bp_array)
print("Blood sugar levels:", sugar_array)

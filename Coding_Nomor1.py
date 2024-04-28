import pandas as pd
import numpy as np

# Membaca dataset
df = pd.read_csv("https://raw.githubusercontent.com/robbyhdayatt/UTS-PDT/main/output.csv")

df = pd.read_csv("https://raw.githubusercontent.com/robbyhdayatt/UTS-PDT/main/output.csv")
df

df.info()

# Informasi statistik data
df.describe()

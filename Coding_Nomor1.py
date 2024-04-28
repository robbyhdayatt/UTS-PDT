import pandas as pd
import numpy as np

# Membaca dataset
df = pd.read_csv("https://raw.githubusercontent.com/robbyhdayatt/UTS-PDT/main/output.csv")

df = pd.read_csv("https://raw.githubusercontent.com/robbyhdayatt/UTS-PDT/main/output.csv")
df

df.info()

# Informasi statistik data
df.describe()

# Menghitung jumlah
total = df['Video Uploads'].sum()

# Menghitung rata-rata
mean = df['Video Uploads'].mean()

# Menghitung median
median = df['Video Uploads'].median()

print("Video Uploads")
print("Jumlah:", total)
print("Rata-rata:", mean)
print("Median:", median)

# Menghitung jumlah
total = df['Video views'].sum()

# Menghitung rata-rata
mean = df['Video views'].mean()

# Menghitung median
median = df['Video views'].median()

print("Video views")
print("Jumlah:", total)
print("Rata-rata:", mean)
print("Median:", median)

# Menghitung jumlah
total = df['Subscribers'].sum()

# Menghitung rata-rata
mean = df['Subscribers'].mean()

# Menghitung median
median = df['Subscribers'].median()

print("Subscribers")
print("Jumlah:", total)
print("Rata-rata:", mean)
print("Median:", median)

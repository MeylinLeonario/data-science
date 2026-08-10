import pandas as pd

df = pd.read_csv('modified_data.csv')

# Cantidad de nulos por columna
one = df.isnull().sum()

# ¿Existe algún nulo?
two = df.isnull().values.any()

# Total de nulos en todo el dataset
three = df.isnull().sum().sum()

# Filas que contienen al menos un nulo
four = df[df.isnull().any(axis=1)]

# Porcentaje de nulos por columna
five = df.isnull().mean() * 100

print(one)
print(two)
print(three)
print(four)
print(five)
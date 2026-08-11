import pandas as pd

df = pd.read_csv('clientes_nulos.csv')

print(df.isnull().sum())

df["edad"] = df["edad"].fillna(df["edad"].mode()[0])

df["ciudad"] = df["ciudad"].fillna(df["ciudad"].mode()[0])

df["ingreso_mensual"] = df["ingreso_mensual"].fillna(df["ingreso_mensual"].mean())

df["cliente_premium"] =df["cliente_premium"].fillna("No")

df["satisfaccion"] = df["satisfaccion"].fillna(df["satisfaccion"].median())

df["compras"] = df["compras"].fillna(df["compras"].mean())

df.to_csv("clientes_limpios.csv", index=False)
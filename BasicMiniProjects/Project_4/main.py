import pandas as pd

df = pd.read_csv("clientes_limpios.csv")

df["edad"] = df["edad"].astype("int64")

df["compras"] = df["compras"].astype("int64")
df["satisfaccion"] = df["satisfaccion"].astype("int64")

df["cliente_premium"] = df["cliente_premium"].map({
    "Si": True,
    "No": False
})

df["nombre"] = df["nombre"].astype("string")
df["ciudad"] = df["ciudad"].astype("category")

df.to_csv("clientes_corregidos.csv", index=False)
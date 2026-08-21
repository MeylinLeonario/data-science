import pandas as pd

df = pd.read_csv("clientes.csv")

print(df[
    (df["edad"]>=30) &
    (df["ingreso_mensual"] >= 1000000)
])
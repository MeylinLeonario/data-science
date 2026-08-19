import pandas as pd

df = pd.read_csv("clientes_limpios.csv")

df.sort_values(
    by=["edad", "ingreso_mensual"],
    ascending=[True, False],
    inplace=True
)

print(df)
# Encontrar valores nulos

Para esta ocasión, encontaremos los valores nulos de cada fila. Esto, con el objetivo de saber.

Para ello, tenemos los siguientes comandos:
- `df.isnull().sum()`: devuelve cantidd de nulos por columna.
- `df.isnul().values.any()`: devuelve si hay al menos un nulo por columna.
- `df.isnull().sum().sum()`: devuelve el total de nulos en todo el dataset.
- `df[df.isnull().any(axis=1)]`: devuelve filas que contienen al menos un nulo.
- `df.isnull().mean() * 100`: porcentaje de nulos por columna.

### Observaciones
- También podemos usar `.isna()`.
# Reemplazar valores nulos

Cuando existen valores nulos en una columna, debemos tener en consideración qué clase de valores nulos son para poder saber qué podríamos hacer con éstos.

| Tipo de dato      | Reemplazo típico            | Cuándo usarlo                                         |
| ----------------- | --------------------------- | ----------------------------------------------------- |
| Numérico          | **Media**                   | Datos relativamente simétricos, sin muchos outliers   |
| Numérico          | **Mediana**                 | Hay outliers o valores extremos                       |
| Numérico          | **Moda**                    | Hay pocos valores posibles/repetidos                  |
| Categórico        | **Moda**                    | Falta poca información                                |
| Categórico        | `"Desconocido"`             | Que falte el dato puede ser información útil          |
| Booleano          | `False` / moda              | Solo si tiene sentido semánticamente                  |
| Fecha             | No siempre conviene imputar | Depende de qué representa la fecha                    |
| Cualquier columna | Eliminar fila               | Si son muy pocos nulos y perder esas filas no importa |

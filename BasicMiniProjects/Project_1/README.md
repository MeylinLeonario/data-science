# Leer un CSV y mostrar estadísticas generales

<table>
    <tr>
        <td width="70%" valign="middle">
        Objetivo: leer un CSV y mostrar estadísticas generales: la moda, la medina
        y la media. 
        Algo sencillo para empezar a refrescar la memoria.
        </td>
        <td>
            <img src="tile005.png">
        </td>
    </tr>
</table>

## Lógica de cómo leer un archivo
Para leer un archivo, primeramente requerimos de abrir el achivo. Una vez tenemos el archivo abierto, leeremos los datos y los guardaremos/procesaremos.

Una vez abierto el archivo, se tiene que volver a cerrar.

### Condieraciones
* Abrir el archivo no es lo mismo que leer el archivo: un archivo puede estar abierto y sin embargo no leído. 
Al nosotros hacer `archivo = open("nombre_archivo.csv", "r")`, estamos dando paso abrir el archivo en modo lectura, no a leer cada dato dentro de las filas del archivo.

* Si queremos guardar el contenido del archivo en listas, debemos de primero tener las listas vacías y luego hacer append por cada fila leída.

* next(lector) indica que **no** se leerá la primera fila; en nuesto caso es porque indica que tiene strings que explican las demás filas.
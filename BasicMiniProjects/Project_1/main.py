import csv
import statistics

""" Se abre modified_data.csv para ver los datos en modo lectura (r)"""
date = []
price = []
bedrooms = []
bathrooms = []
sqft_living = []
sqft_lot = []
floors = []
waterfront = []
view = []
condition = []
sqft_above = []
sqft_basement = []
yr_built = []
yr_renovated = []
street = []
city = []
statezip = []
price_per_sqft = []

with open("modified_data.csv", "r") as archivo:
    lector = csv.reader(archivo)

    next(lector)
    
    for fila in lector:
        date.append(fila[0])
        price.append(float(fila[1]))
        bedrooms.append(float(fila[2]))
        bathrooms.append(float(fila[3]))
        sqft_living.append(float(fila[4]))
        sqft_lot.append(float(fila[5]))
        floors.append(float(fila[6]))
        waterfront.append(float(fila[7]))
        view.append(float(fila[8]))
        condition.append(float(fila[9]))
        sqft_above.append(float(fila[10]))
        sqft_basement.append(float(fila[11]))
        yr_built.append(float(fila[12]))
        yr_renovated.append(float(fila[13]))
        street.append(fila[14])
        city.append(fila[15])
        statezip.append(fila[16])
        price_per_sqft.append(float(fila[17]))

# ================= CÁLCULOS =================
# mediana de price
mediana = statistics.mean(price)

# media de bedrooms
media_bedrooms = statistics.median(bedrooms)

# moda de bathrooms
moda_bathrooms = statistics.mode(bathrooms)

print(f"Mediana de price: {mediana}")
print(f"Media de bedrooms: {media_bedrooms}")
print(f"Moda de bathrooms: {moda_bathrooms}")
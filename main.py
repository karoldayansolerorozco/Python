# Importar librerías necesarias
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Importar la librería pandas para manejar estructuras de datos
import pandas as pd

# Crear un diccionario con datos ficticios
data = {
    'Nombre': ['Tom', 'Jerry', 'Mickey', 'Goofy'],  # Lista de nombres
    'Edad': [20, 21, None, 18],                     # Lista de edades, incluyendo un valor faltante (None)
    'Genero': ['M', 'M', 'M', 'F'],                 # Lista de géneros ('M' para masculino, 'F' para femenino)
    'Salario': [500, 520, 480, None]                # Lista de salarios, incluyendo un valor faltante (None)
}

# Crear un DataFrame de pandas a partir del diccionario de datos
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

#Eliminar datos duplicados 
df.drop_duplicates(inplace=True)


# Mostrar el DataFrame después de eliminar duplicados
print("\nDataFrame después de eliminar duplicados:")
print(df)

# Crear un imputador que reemplazará los valores faltantes con la media de la columna
imputer = SimpleImputer(strategy='mean')

# Imputar los valores faltantes en la columna 'Edad'
# Utilizamos .values.reshape(-1, 1) para transformar la columna en un arreglo de 2D requerido por SimpleImputer
df['Edad'] = imputer.fit_transform(df[['Edad']])

# Convertir la columna 'Edad' a enteros después de la imputación
df['Edad'] = df['Edad'].astype(int)

#Codificar varibales categoricas
Label_encoder= LabelEncoder()
df['Genero']= Label_encoder.fit_transform(df['Genero'])


# Imputar los valores faltantes en la columna 'Salario'
# Utilizamos .values.reshape(-1, 1) para transformar la columna en un arreglo de 2D requerido por SimpleImputer
df['Salario'] = imputer.fit_transform(df[['Salario']])


# Mostrar el DataFrame después de la imputación de la columna 'Edad'
print("\nDataFrame después de imputar valores faltantes en 'Edad':")
print(df)
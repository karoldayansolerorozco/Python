## Uso

Para ejecutar el script y ver el procesamiento de datos, sigue estos pasos:

1. Ejecuta el script de Python:
    ```bash
    python script.py
    ```

2. Observa la salida en la consola para ver el DataFrame antes y después del procesamiento. La salida mostrará cómo se eliminaron los duplicados, se imputaron los valores faltantes y se convirtieron a enteros.

### Ejemplo de Uso

El script realiza las siguientes acciones:

- Crea un DataFrame con datos ficticios y algunos valores faltantes.
- Elimina filas duplicadas.
- Imputa los valores faltantes en la columna 'Edad' con la media de la columna.
- Convierte la columna 'Edad' a enteros.

Aquí está el código completo del script:

```python
# Importar la librería pandas para manejar estructuras de datos
import pandas as pd
from sklearn.impute import SimpleImputer  # Importar SimpleImputer para imputar valores faltantes

# Crear un diccionario con datos ficticios
data = {
    'Nombre': ['Tom', 'Jerry', 'Mickey', 'Goofy'],  # Lista de nombres
    'Edad': [20, 21, None, 18],                     # Lista de edades, con un valor faltante (None)
    'Genero': ['M', 'M', 'M', 'F'],                 # Lista de géneros
    'Salario': [500, 520, 480, None]                # Lista de salarios, con un valor faltante (None)
}

# Crear un DataFrame de pandas a partir del diccionario de datos
df = pd.DataFrame(data)

# Mostrar el DataFrame original con valores faltantes
print("DataFrame original:")
print(df)

# Eliminar filas duplicadas en el DataFrame
df.drop_duplicates(inplace=True)

# Crear un imputador que reemplazará los valores faltantes con la media de la columna
imputer = SimpleImputer(strategy='mean')

# Imputar los valores faltantes en la columna 'Edad'
df['Edad'] = imputer.fit_transform(df[['Edad']])

# Convertir la columna 'Edad' a enteros después de la imputación
df['Edad'] = df['Edad'].astype(int)

# Mostrar el DataFrame después de la imputación de la columna 'Edad' y la conversión a entero
print("\nDataFrame después de imputar valores faltantes en 'Edad' y convertir a enteros:")
print(df)

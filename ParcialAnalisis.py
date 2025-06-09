import pandas as pd

# URL directa al archivo CSV en OneDrive (REEMPLAZA AQUÍ TU LINK)
url = "https://raw.githubusercontent.com/itsWalter507/ParcialIA/refs/heads/main/dataset_sistema.csv"

# Cargar dataset desde OneDrive
df = pd.read_csv(url)

# Columnas numéricas relevantes (sin GPU)
numericas = ['cpu_total', 'ram_total', 'disk_total', 'cpu_proc', 'ram_proc']

# Verificar columnas con datos válidos
numericas_disponibles = [col for col in numericas if df[col].notna().sum() > 0]

# Filtrar y limpiar
df_numericas = df[numericas_disponibles].dropna()

print("\n--- ESTADÍSTICAS BÁSICAS ---")
print("\nMedia:\n", df_numericas.mean())
print("\nMediana:\n", df_numericas.median())

try:
    print("\nModa:\n", df_numericas.mode().iloc[0])
except IndexError:
    print("\nModa: No se pudo calcular (dataset vacío o sin datos válidos)")

print("\nDesviación estándar:\n", df_numericas.std())

print("\n--- MATRIZ DE CORRELACIÓN ---")
print(df_numericas.corr())
import psutil
import pandas as pd
import time

data = []

print("Recolectando datos...")

# Número de muestras (ajusta para alcanzar 5000 registros o más)
for _ in range(10):  # Aumenta a 500+ para un dataset grande
    timestamp = time.time()
    cpu_total = psutil.cpu_percent(interval=0.1)
    ram_total = psutil.virtual_memory().percent
    disk_total = psutil.disk_usage('/').percent

    # Capturar todos los procesos
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info
            data.append({
                'timestamp': timestamp,
                'cpu_total': cpu_total,
                'ram_total': ram_total,
                'disk_total': disk_total,
                'pid': info['pid'],
                'name': info['name'],
                'cpu_proc': info['cpu_percent'],
                'ram_proc': info['memory_percent'],
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

# Guardar en CSV
df = pd.DataFrame(data)
df.to_csv('dataset_sistema.csv', index=False)
print("✅ Dataset guardado como 'dataset_sistema.csv'")
from pymongo import MongoClient
import datetime
import random
import names

# Conexión a la base de datos MongoDB
client = MongoClient('localhost', 27017)
db = client['trabajadores']
collection = db['info']

def agregar_trabajador(nombre, fecha_nacimiento, sueldo):
    trabajador = {
        'nombre': nombre,
        'fecha_nacimiento': fecha_nacimiento,
        'sueldo': sueldo,
        'fecha_registro': datetime.datetime.now()
    }
    collection.insert_one(trabajador)

def generar_fecha_nacimiento():
    year = random.randint(1970, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Considerando febrero
    return f"{year:04d}-{month:02d}-{day:02d}"

def generar_sueldo():
    return round(random.uniform(1500, 5000), 2)

if __name__ == "__main__":
    for _ in range(3):
        nombre = names.get_full_name()
        fecha_nacimiento = generar_fecha_nacimiento()
        sueldo = generar_sueldo()
        
        agregar_trabajador(nombre, fecha_nacimiento, sueldo)
    
    # Imprimir los trabajadores almacenados en la base de datos
    print("Trabajadores almacenados en la base de datos:")
    for trabajador in collection.find():
        print(f"Nombre: {trabajador['nombre']}")
        print(f"Fecha de Nacimiento: {trabajador['fecha_nacimiento']}")
        print(f"Sueldo: {trabajador['sueldo']}")
        print("---------------------------")

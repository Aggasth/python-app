from pymongo import MongoClient
import datetime

# Conexión a la base de datos MongoDB
client = MongoClient('localhost', 27017)
db = client['trabajadores']
collection = db['info']

trabajadores = [
    {
        'nombre': 'Juan Pérez',
        'fecha_nacimiento': '1990-05-15',
        'sueldo': 2500.50,
        'sexo': 'Masculino'
    },
    {
        'nombre': 'María López',
        'fecha_nacimiento': '1985-11-03',
        'sueldo': 3200.75,
        'sexo': 'Femenino'
    },
    {
        'nombre': 'Carlos Rodríguez',
        'fecha_nacimiento': '1988-02-22',
        'sueldo': 2900.25,
        'sexo': 'Masculino'
    },
    {
        'nombre': 'Ana Martínez',
        'fecha_nacimiento': '1992-07-10',
        'sueldo': 2100.80,
        'sexo': 'Femenino'
    },
    {
        'nombre': 'Luis Gómez',
        'fecha_nacimiento': '1995-09-28',
        'sueldo': 1800.60,
        'sexo': 'Masculino'
    }
]

def agregar_trabajador(trabajador):
    trabajador['fecha_registro'] = datetime.datetime.now()
    collection.insert_one(trabajador)

if __name__ == "__main__":
    for t in trabajadores:
        agregar_trabajador(t)
    
    # Imprimir los trabajadores almacenados en la base de datos
    print("Trabajadores almacenados en la base de datos:")
    for trabajador in collection.find():
        print(f"Nombre: {trabajador['nombre']}")
        print(f"Fecha de Nacimiento: {trabajador['fecha_nacimiento']}")
        print(f"Sueldo: {trabajador['sueldo']}")
        print(f"Sexo: {trabajador['sexo']}")
        print("---------------------------")


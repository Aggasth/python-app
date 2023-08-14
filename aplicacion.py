from pymongo import MongoClient
import datetime

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
    print("Trabajador agregado exitosamente.")

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del trabajador: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
    sueldo = float(input("Ingrese el sueldo del trabajador: "))
    
    agregar_trabajador(nombre, fecha_nacimiento, sueldo)

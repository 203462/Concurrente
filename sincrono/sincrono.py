import requests
import time
import psycopg2

try:
    conexion = psycopg2.connect(
        host="localhost",
        database='Concurrente1', 
        user='postgres', 
        password='203462')
    cursor=conexion.cursor()
    cursor.execute('select version()')
    version=cursor.fetchone()
except Exception as err:
    print('Sucedió un error al conectar a la base de datos')


def service():
    get_service()

def get_service():
    url = "https://jsonplaceholder.typicode.com/photos"
    r = requests.get(url)
    data = r.json()
    photos = data
    for photo in photos:
        write_db(photo["title"])

def connect_db():
    pass

def close_conexion():
    conexion.close()

def write_db(title):
    try:
        cursor.execute("insert into title (name) values ('"+title+"')")
    except Exception as err:
        print('Hubo un error en la inserción: '+ err)
    else:
        conexion.commit()

if __name__ == "__main__":
    init_time = time.time()
    service()
    end_time = time.time() - init_time
    print(end_time)
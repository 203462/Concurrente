import pytube
import concurrent.futures
import threading
import time
import psycopg2
import requests

#array contains links videos
enlaces = (
    'https://www.youtube.com/watch?v=i13yFolV-wk',
    'https://www.youtube.com/watch?v=kSv6qlPtvR0',
    'https://www.youtube.com/watch?v=m6jfZa00vkY',
    'https://www.youtube.com/watch?v=dONYu8lfOzw',
    'https://www.youtube.com/watch?v=jhvfYsYQXkc')

#function to connect a database"
try:
    conexion = psycopg2.connect(
        host="127.0.0.1",
        database='Concurrente1',
        user='postgres',
        password='203462')
    cursor = conexion.cursor()
    cursor.execute('select version()')
    version = cursor.fetchone()
except Exception as err:
    print('Sucedió un error al conectar a la base de datos')

#functiion to the get the titles of photos
def write_nombres():
    url = "https://jsonplaceholder.typicode.com/photos"
    r = requests.get(url)
    data = r.json()
    photos = data
    for photo in photos:
        write_db(photo["title"])
    print("Se ha completado la inserción de los 5000 datos")

#function to write the 5000 titles the photos in the database
def write_db(title):
    try:
        cursor.execute("insert into title (name) values ('"+title+"')")
    except Exception as err:
        print('Hubo un error en la inserción: ' + err)
    else:
        conexion.commit()

#function to dowload videos 
def download_videos(enlaces):
    for x in range (5):
        video = pytube.YouTube(enlaces[x])
        video.streams.first().download("C:/Descargas")
    print(f'{enlaces} se ha descargado...')
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_videos, enlaces)


#Function to get the 50 names
def get_services(dato=0):
    print(f'Dato={dato}')
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)


#MAIN 
if __name__ == '__main__':
    th1 = threading.Thread(target=write_nombres)
    th2 = threading.Thread(target=download_videos, args=[enlaces])
    th1.start()
    th2.start()
    th2.join()
    for x in range(0, 50):
        th3 = threading.Thread(target=get_services, args=[x])
        th3.start()
    
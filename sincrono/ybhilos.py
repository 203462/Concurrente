import threading
import concurrent.futures
from pprint import pprint
import json
import time
import pytube 
guardar = "C:/Descargas/"
url = ["https://www.youtube.com/watch?v=I8c7UBa_0nk","https://www.youtube.com/watch?v=fHR1CZ9x61E","https://www.youtube.com/watch?v=sbLqX7cUKoM","https://www.youtube.com/watch?v=hoQmSA6MRAk","https://www.youtube.com/watch?v=sfQOiDJX-x4"]
threading_local = threading.local()

def get_service():
    video0 = pytube.YouTube(url[0])
    video0.streams.first().download(guardar)

    video1 = pytube.YouTube(url[1])
    video1.streams.first().download(guardar)

    video2 = pytube.YouTube(url[2])
    video2.streams.first().download(guardar)

    video3 = pytube.YouTube(url[3])
    video3.streams.first().download(guardar)

    video4 = pytube.YouTube(url[4])
    video4.streams.first().download(guardar)

def servicio():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service)
        
if __name__ == "__main__":
    get_service()
    init_time = time.time()
    get_service()
    end_time = time.time() - init_time
    print(end_time)
    

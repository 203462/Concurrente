from threading import Thread, Semaphore
import pytube 
semaforo = Semaphore(1) 

enlaces = [
        'https://www.youtube.com/watch?v=i13yFolV-wk',
        'https://www.youtube.com/watch?v=kSv6qlPtvR0',
        'https://www.youtube.com/watch?v=m6jfZa00vkY',
        'https://www.youtube.com/watch?v=1GnyvSlPSTU',
        'https://www.youtube.com/watch?v=jhvfYsYQXkc'
    ]# se crea la variable de semaforo


def descarga(id):
    
    yt = pytube.YouTube(enlaces[id])
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download("C:/Users/angel")
    print(f'{enlaces[id]} se esta descargando...')


class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        semaforo.acquire()  # se inicia el semaforo
        descarga(self.id)
        semaforo.release()  # libera el semaforo e incrementa la variable semaforo


threads_semaphore = [Hilo(0), Hilo(1), Hilo(2), Hilo(3), Hilo(4)]
for i in threads_semaphore:
    i.start()

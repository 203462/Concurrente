import pytube
import concurrent.futures
import threading
import time




enlaces = [
    'https://www.youtube.com/watch?v=i13yFolV-wk',
    'https://www.youtube.com/watch?v=kSv6qlPtvR0',
    'https://www.youtube.com/watch?v=m6jfZa00vkY',
    'https://www.youtube.com/watch?v=1GnyvSlPSTU',
    'https://www.youtube.com/watch?v=jhvfYsYQXkc'
]

t1 = time.perf_counter()


def download_videos(enlaces):
    yt = pytube.YouTube(enlaces)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download("C:/Users/angel")
    print(f'{enlaces} se esta descargando...')
with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_videos, enlaces)


t2 = time.perf_counter()

print (f'Se ha finalizado en: {t2-t1} segundos')

if __name__ == "__main__":
    download_videos(enlaces)

import threading

locked = threading.Lock()


def mesa(persona):
    global x
    x = 2
    print("-------------------------------")
    print("La persona " + str(persona) + " tiene " + str(x) + " palillos y ha empezado a comer")


class Hilo(threading.Thread):
    def __init__(self, persona):
        threading.Thread.__init__(self)
        self.persona = persona

    def run(self):
        locked.acquire()
        mesa(self.persona)
        locked.release()
        print("dejo de comer")


hilos = [Hilo(1), Hilo(2), Hilo(3), Hilo(
    4), Hilo(5), Hilo(6), Hilo(7), Hilo(8)]
for h in hilos:
    h.start()  
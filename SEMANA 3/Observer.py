#patrón Observer
#Eddie Girón y Julio Ruíz
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)


class Observer:
    def update(self, data):
        pass


class ConcreteSubject(Subject):
    def do_something(self):
        # Realiza una acción y notifica a los observadores
        data = "Algo ha sucedido"
        self.notify(data)


class ConcreteObserver(Observer):
    def update(self, data):
        print(f"Observador ha recibido la notificación: {data}")


# Uso del patrón Observer
subject = ConcreteSubject()

observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

subject.do_something()

subject.detach(observer2)

subject.do_something()
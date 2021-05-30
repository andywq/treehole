class Notifier(object):
    def __init__(self):
        self.observers = []

    def getNum(self, num):
        for ob in self.observers:
            ob.receive(num)

class AddObserver(object):
    def __init__(self, notifier):
        notifier.observers.append(self)
        self.result = 0

    def receive(self, num):
        self.result = num + 1

class SubObserver(object):
    def __init__(self, notifier):
        notifier.observers.append(self)
        self.result = 0

    def receive(self, num):
        self.result = num - 1

class Product(object):
    def identify(self):
        return self.__class__

class Car(Product): pass
class Truck(Product): pass

class SimpleFactory(object):
    def getProduct(self, product_name):
        if globals().get(product_name):
            return globals().get(product_name)()

# factory method
class CarFactory(object):
    def getProduct(self):
        return Car()

class TruckFactory(object):
    def getProduct(self):
        return Truck()

# abstract factory
class FooCar(Car):
    brand = 'Foo'
class FooTruck(Truck):
    brand = 'Foo'
class BarCar(Car):
    brand = 'Bar'
class BarTruck(Truck):
    brand = 'Bar'

class FooFactory(object):
    def getCar(self):
        return FooCar()
    def getTruck(self):
        return FooTruck()

class BarFactory(object):
    def getCar(self):
        return BarCar()
    def getTruck(self):
        return BarTruck()

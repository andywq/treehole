import unittest

import singleton
import factory
import observer

class TestDesignPattern(unittest.TestCase):
    def test_singleton(self):
        sg1 = singleton.Singleton()
        sg2 = singleton.Singleton()

        self.assertTrue(sg1 is sg2)
        self.assertTrue(isinstance(sg1, singleton.Singleton))

    def test_simple_factory(self):
        sf = factory.SimpleFactory()

        self.assertTrue(sf.getProduct('Car').identify() is factory.Car)
        self.assertTrue(sf.getProduct('Truck').identify() is factory.Truck)
        self.assertTrue(sf.getProduct('NotExists') is None)

    def test_factory_method(self):
        cf = factory.CarFactory()
        tf = factory.TruckFactory()

        self.assertTrue(cf.getProduct().identify() is factory.Car)
        self.assertTrue(tf.getProduct().identify() is factory.Truck)

    def test_abstact_factory(self):
        ff = factory.FooFactory()
        bf = factory.BarFactory()

        fcar = ff.getCar()
        ftruck = ff.getTruck()
        bcar = bf.getCar()
        btruck = bf.getTruck()

        self.assertTrue(isinstance(fcar, factory.Car) and 'Foo' == fcar.brand)
        self.assertTrue(isinstance(ftruck, factory.Truck) and 'Foo' == ftruck.brand)
        self.assertTrue(isinstance(bcar, factory.Car) and 'Bar' == bcar.brand)
        self.assertTrue(isinstance(btruck, factory.Truck) and 'Bar' == btruck.brand)

    def test_observer(self):
        nt = observer.Notifier()
        ao = observer.AddObserver(nt)
        so = observer.SubObserver(nt)
        num = 2

        nt.getNum(num)
        self.assertEqual(ao.result, num + 1)
        self.assertEqual(so.result, num - 1)

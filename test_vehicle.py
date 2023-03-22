"""
Tests for vehicle
"""

import unittest
class TestVehicle(unittest.TestCase):
    """
    Test for Vehicle class
    """
    def test_vehicle_init(self):
        """
        Test vehicle init
        """
        v1 = Vehicle("Zorith", 2)
        self.assertEqual(str(v1), "Zorith holds 2: [], free 2")
        self.assertEqual(v1.is_empty(), True)

    def test_passager_init(self):
        """
        Test passager init and string represenation
        """
        p1 = Passenger('Arman')
        p2 = Passenger('Armana')
        self.assertEqual(str(p1),"Arman is passenger of ...")
    def test_add_passenger(self):
        """
        Test add passenger
        """
        v1 = Vehicle("Zorith", 2)
        p1 = Passenger('Arman')
        p2 = Passenger('Armana')
        p3= Passenger("Bob")
        self.assertEqual(v1.add_passenger(p1), True)
        self.assertEqual(p1.place , v1)
        self.assertEqual(p1._Passenger__place , v1 )
        self.assertEqual (str(p1) ,"Arman is passenger of Zorith")
        self.assertEqual(v1.add_passenger(p1) ,  False)
        self.assertEqual(v1.add_passenger(p3) ,  True)
        self.assertEqual(v1.add_passenger(p2), False)
    def test_vehicle_capicity(self):
        """
        test Vehicle max capicity
        """
        p1 = Passenger('Arman')
        p2 = Passenger('Armana')
        p3 = Passenger("Arcana")
        v1 = Vehicle("Zorith", 2)
        v1.add_passenger(p1)
        v1.add_passenger(p2)
        self.assertEqual(v1.add_passenger(p3) , False)
        self.assertEqual(str(v1) , "Zorith holds 2: ['Arman', 'Armana'], free 0")
        # can remove the most recent passenger
        self.assertEqual(v1.remove_passenger() , p2)
        self.assertEqual(str(v1) , "Zorith holds 2: ['Arman'], free 1")
        self.assertEqual(v1.add_passenger(p3) , True)
    def test_bus_compare(self):
        """
        Test bus compare
        """
        v1 = Vehicle("Zorith", 2)
        path = "Lviv - Stari Kuty"
        v2 = Bus("Bus", 20, path)
        self.assertEqual(v2 ,Bus("Bus", 20, path))
        self.assertNotEqual(v2 , Bus("Bus", 20, "Lviv - Tuziliv"))
        self.assertNotEqual(v2 , v1)
        self.assertNotEqual(v2 , "Bus")
        self.assertNotEqual(v2 ,7)
    def test_bus_remove(self):
        """
        Test remove for bus class
        """
        path = "Lviv - Stari Kuty"
        p2 = Passenger('Armana')
        p3 = Passenger('Bob')
        v2 = Bus("Bus", 20, path)
        self.assertEqual(v2.remove_passenger() , False)
        self.assertEqual(v2.add_passenger(p2) , True)
        self.assertEqual(str(v2) , "Bus holds 20: ['Armana'], free 19")
        self.assertEqual(v2.remove_passenger(), (p2, "Bus is empty!"))
        self.assertEqual(v2.remove_passenger() , False)
    def test_buggy_methods(self):
        """
        Test buggy methods
        """
        b1 = Buggy("ADC Buggy")
        p4 = Driver("Driver")
        self.assertEqual(b1.add_passenger(p4),  True)
        self.assertEqual(p4.place, b1)
        self.assertEqual(str(b1), "ADC Buggy holds 1: ['Driver'], free 0")
        
    def test_pushing_buggy(self):
        """
        Test pushing buggy
        """
        b1 = Buggy("ADC Buggy")
        p4 = Driver("Driver")
        b1.add_passenger(p4)
        b1.start_pushing()
        self.assertEqual(b1.remove_passenger() , False)
        b1.stop_pushing()
        self.assertEqual(b1.remove_passenger() == p4)
        self.assertEqual(b1.remove_passenger() == False)
    def test_buggy_eq(self):
        """
        Test equality for buggy
        """
        b2 = Buggy("SD Buggy")
        b3 = Buggy("DC Buggy")
        self.assertEqual(b2, Buggy("SD Buggy"))
        self.assertNotEqual (b2 , b3)
        self.assertNotEqual (b2 , "adsasdas")
        self.assertNotEqual (b2 , 6)
        self.assertEqual(Buggy.buggy_count() == 4)
    def test_garage(self):
        """
        Test garage
        """
        b1 = Buggy("ADC Buggy")
        v1 = Vehicle("Zorith", 2)
        garage = set()
        self.assertNotIn( v1 , garage)
        garage.add(v1)
        self.assertIn( v1 , garage)
        self.assertNotIn( b1 , garage)
        garage.add(b1)
        self.assertIn( b1, garage)
        garage.remove(b1)
        self.assertNotIn( b1 , garage)
unittest.main(argv=[''], verbosity=2, exit=False)

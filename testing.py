import unittest
from main import HaromszogEgyenlotlenseg

class Testing(unittest.TestCase):
    def setUp(self):
        print("setting up testing")
        self.tester = HaromszogEgyenlotlenseg()

    def teszt_nem_szerkesztheto_haromszog(self):
        print("Teszt 1: nem szerkeszthető háromszög")
        self.assertEqual(self.tester.haromszog_egyenlotlenseg_vizsgalo(2,2,5), False, "Nem szerkeszthető háromszög!")

    def teszt_haromszog_szerkesztheto(self):
        print("Teszt 2: szerkeszthető háromszög")
        self.assertEqual(self.tester.haromszog_egyenlotlenseg_vizsgalo(3,3,5), True, "Szerkeszthető háromszög!")

    def test_TypeError(self):
        print("Teszt 3: típushiba")
        with self.assertRaises(TypeError):
            result = self.tester.haromszog_egyenlotlenseg_vizsgalo("Macbook Air", "M2", 15)

    def tearDown(self):
        print("tearing down")

if __name__ == "__main__":
    unittest.main()
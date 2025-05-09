from unittest import TestCase
from paths import places_generator

class Test(TestCase):
    def test_places_generator(self):
        p = places_generator()
        self.assertIsNotNone(p)

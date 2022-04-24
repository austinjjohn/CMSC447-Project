from django.test import TestCase
from Haven.models import EvacLocation
from django.utils import timezone

# Create your tests here.
class LocationTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_createLocation(self):
        test = EvacLocation(address='1000 hilltop cir', pets=0, spaces=3, reservations=2, pub_date=timezone.now())
        test.create('1000 hilltop cir', 0, 3, 2, timezone.now())
        test.save()
        test.allows_pets()
        test.get_spaces()
        test.was_published_recently()
        test.is_full()
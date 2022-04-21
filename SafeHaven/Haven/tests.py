from django.test import TestCase
from django.utils import timezone
from Haven.models import EvacLocation, Volunteer, Evacuee
# Create your tests here.

class LocationTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_createLocation(self):
        test = EvacLocation(address='1000 hilltop cir', pets=0, spaces=3, reservations=2, pub_date=timezone.now())
        test.allows_pets()
        test.get_spaces()
        test.was_published_recently()
        test.is_full()

class VolunteerTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Volunteer(self):
        volunteer = Volunteer(name="Jeremy")
        volunteer.dict()

class EvacueeTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Evacuee(self):
        evacuee = Evacuee(name="Jake", pets=2, spaces_needed=1)
        evacuee.dict()
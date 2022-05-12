from django.utils import timezone
from Haven.models import EvacLocation, Volunteer, Evacuee
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

options = webdriver.ChromeOptions()
options.headless = False  # Make this True you want this program to run headless
options.add_experimental_option('excludeSwitches', ['enable-logging'])


# Create your tests here.
class UserSignup(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver.exe', options=options)
    def tearDown(self):
        self.browser.close()

    def test_redirect_to_signup_with_selenium(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Login').click()
        title_text = self.browser.find_element(By.TAG_NAME, 'h2').text
        self.assertEquals(title_text, 'Register a New Account')

    def test_user_object_saved(self):
        test = User(username='testuser',
                    password='Thisisasecrettestpassowrd',
                    email='testemail@gmail.com',
                    first_name='firstname',
                    last_name='lastname')
        test.save()
        q1 = User.objects.filter(username__startswith='testuser')  # q1 = EvacLocation.objects.get(pk=test.pk) #Can also use this line
        self.assertTrue(q1)

    # Not working at the moment
    def test_valid_user_saved_with_selenium(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Login').click()
        self.browser.find_element(By.NAME, 'first_name').send_keys('firstname2')
        self.browser.find_element(By.NAME, 'last_name').send_keys('lastname2')
        self.browser.find_element(By.NAME, 'username').send_keys('testuser2')
        self.browser.find_element(By.NAME, 'email').send_keys('testemail2@gmail.com')
        self.browser.find_element(By.NAME, 'password1').send_keys('Thisisasecrettestpassowrd2')
        self.browser.find_element(By.NAME, 'password2').send_keys('Thisisasecrettestpassowrd2')
        self.browser.find_element(By.CLASS_NAME, 'btn').click()

        q2 = User.objects.values()
        self.assertEquals(q2[0]['username'], 'testuser2')

class VolunteerTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver.exe', options=options)

    def tearDown(self):
        self.browser.close()

    def test_redirect_to_volunteer_with_selenium(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Volunteer').click()
        title_text = self.browser.find_element(By.TAG_NAME, 'h2').text
        self.assertEquals(title_text, 'Volunteer Profile')

    def test_volunteer_object_saved(self):
        test = EvacLocation(address='1000 hilltop cir', pets=0, spaces=3, reservations=2, pub_date=timezone.now())
        test.save()
        q1 = EvacLocation.objects.filter(address__startswith='1000 hilltop cir') #q1 = EvacLocation.objects.get(pk=test.pk) #Can also use this line
        self.assertTrue(q1)

    # This test does not work yet, there for it is excluded
    def _test_valid_user_saved_with_selenium(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Volunteer').click()
        self.browser.find_element(By.NAME, 'address').send_keys('2000 hilltop cir')
        self.browser.find_element(By.NAME, 'pets').send_keys('1')
        self.browser.find_element(By.NAME, 'spaces').send_keys('4')
        self.browser.find_element(By.ID, 'partyCount').send_keys('3')
        self.browser.find_element(By.ID, 'partyCount').send_keys(Keys.RETURN)

        #q2 = EvacLocation.objects.filter(address__startswith='2000 hilltop cir')
        q2 = EvacLocation.objects.first()
        self.assertEquals(q2[0]['address'], '2000 hilltop cir')

class EvacueeTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver.exe', options=options)

    def tearDown(self):
        self.browser.close()

    def test_redirect_to_evacuee_with_selenium(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Evacuee').click()
        title_text = self.browser.find_element(By.TAG_NAME, 'h2').text
        self.assertEquals(title_text, 'Evacuee Profile')

    # def test_evacuee(self):
    #     evacuee = Evacuee(name="Jake", pets=2, spaces_needed=1)
    #     evacuee.dict()



# class LocationTest(StaticLiveServerTestCase):
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     def test_createLocation(self):
#         test = EvacLocation(address='1000 hilltop cir', pets=0, spaces=3, reservations=2, pub_date=timezone.now())
#         test.create('1000 hilltop cir', 0, 3, 2, timezone.now())
#         test.save()
#         test.allows_pets()
#         test.get_spaces()
#         test.was_published_recently()
#         test.is_full()
#
#

# class MapTests(TestCase):
#     def test_map_attributes(self):
#         default_map_attributes = {
#             "style": "satellite-streets-v11",
#             "zoom": 14,
#             "center": [-76.71095954472092, 39.25386386415346],
#         }
#         result = {
#             "style": "satellite-streets-v11",
#             "zoom": 14,
#             "center": [-76.71095954472092, 39.25386386415346],
#         }
#         for key in default_map_attributes.keys():
#             self.assertEqual(result[key], default_map_attributes[key])

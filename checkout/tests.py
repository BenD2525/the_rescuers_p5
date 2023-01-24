from django.test import TestCase, Client
from django.urls import reverse


# URL tests
class CheckoutURLTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_checkout_url(self):
        response = self.client.get(reverse('checkout:checkout'))
        self.assertEqual(response.status_code, 200)

    def test_thank_you_url(self):
        response = self.client.get(reverse('checkout:thank_you'))
        self.assertEqual(response.status_code, 200)

    def test_order_success_url(self):
        response = self.client.get(reverse('checkout:order_success'))
        self.assertEqual(response.status_code, 200)

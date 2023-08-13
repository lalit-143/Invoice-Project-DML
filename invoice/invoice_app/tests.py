from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Invoice

class InvoiceAPITest(APITestCase):
    def setUp(self):
        self.invoice_data = {
            "date": "2023-08-13",
            "invoice_no": "INV001",
            "customer_name": "John Doe",
            "invoice_details": [
                {
                    "description": "Product A",
                    "quantity": 2,
                    "unit_price": 10.00,
                    "price": 20.00
                }
            ]
        }

    def test_create_invoice(self):
        url = reverse('invoice-list')
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)

    def test_get_invoices(self):
        url = reverse('invoice-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
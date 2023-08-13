from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    invoice_no = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.invoice_no + " - " + self.customer_name

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit_price = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.invoice.invoice_no + " - " + self.description
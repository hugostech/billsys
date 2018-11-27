from django.db import models
from billingsystem.apps.clients.models import Client

# Create your models here.
class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.FloatField()
    created_date = models.DateField(editable=False,auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.TextField()
    unit_price = models.FloatField()
    quantity = models.IntegerField()

    @property
    def total(self):
        return self.unit_price * self.quantity
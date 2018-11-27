from django.db import models

class Client(models.Model):
    CLIENT_TYPE_CHOICES = (
        ('P', 'Person'),
        ('C', 'Company')
    )
    client_type = models.CharField(max_length=1, choices=CLIENT_TYPE_CHOICES,default='C')
    company_name = models.CharField(max_length=256, blank=True)
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(unique=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    contact_address = models.TextField()
    logo_url = models.URLField(verbose_name='Logo')

    @property
    def balance(self):
        return 0





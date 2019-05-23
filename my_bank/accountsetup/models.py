from django.db import models
#from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Account(models.Model):
    account_number=models.IntegerField()
    account_name=models.CharField(max_length=150)
    #created_date=models.DateTimeField(default=timezone.now())
    balance=models.PositiveIntegerField()
    amount=models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.account_name

    def get_absolute_url(self):
        return reverse('account:accountlist')

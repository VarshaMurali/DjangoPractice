from django import forms
from .models import Account
class DepositForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('amount',)

class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('amount',)

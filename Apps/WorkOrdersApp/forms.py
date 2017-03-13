from django import forms
from .models import Order


class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=['start_date','end_date','coordinator','status','number', 'state','address','client','client_contract','vendor','vendor_sub_out','sub_out']


    def clean(self):
        return self.cleaned_data
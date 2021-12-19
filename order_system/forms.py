from django import forms
from .models import Order


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('total', 'id_restaurant')

from .calculation_utils import calculate_sum_all_products_in_order


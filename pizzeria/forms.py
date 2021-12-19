from django import forms
from .models import PizzeriaLocal


class RestaurantModelForm(forms.ModelForm):
    class Meta:
        model = PizzeriaLocal
        fields = (
            'name', 'address', 'phone_number'
        )
        # widgets = {
        #     'published_date': DateInput(),
        # }
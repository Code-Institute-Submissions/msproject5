from django import forms
from .models import Order
from django.contrib.auth.models import User
from users.models import Profile, User


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = User #Order
        fields = (
            'full_name', 'last_name'
        )

    class Meta:
        model = Profile #Order
        fields = (
            'user_phone_number', 'user_country', 'user_postcode',
            'user_city', 'user_street_address_1', 'user_street_address_2',
            'user_county'
        )
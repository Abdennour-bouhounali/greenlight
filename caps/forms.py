from django import forms

from .models import Donation, Deposit

INPUT_CLASSES = "rounded p-4 w-full bg-gray-200 text-gray-800 placeholder-gray-700 mb-2"

class DonateForm(forms.ModelForm):
    quantity = forms.IntegerField(label='Username', widget=forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Quantity in KG',
    }))
    wilaya = forms.IntegerField(label='Wilaya', widget=forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Wilaya',
    }))
    baladiya = forms.IntegerField(label='Baladiya', widget=forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Baladiya',
    }))
    latitude = forms.FloatField(label='Latitude', widget=forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'style': 'display: none;',
    }))
    longitude = forms.FloatField(label='Longitude', widget=forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'style': 'display: none;',
    }))

    class Meta:
        model = Donation
        fields = ['quantity', 'wilaya', 'baladiya', 'latitude', 'longitude']

    # You can define custom validation or additional behavior for the form if needed
    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic if needed
        return cleaned_data


class DepositForm(forms.ModelForm):
    capacity = forms.IntegerField(label='Username', widget=forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Capacity in KG',
    }))
    wilaya = forms.IntegerField(label='Wilaya', widget=forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Wilaya',
    }))
    baladiya = forms.IntegerField(label='Baladiya', widget=forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Baladiya',
    }))
    latitude = forms.FloatField(label='Latitude', widget=forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'style': 'display: none;',
    }))
    longitude = forms.FloatField(label='Longitude', widget=forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'style': 'display: none;',
    }))

    class Meta:
        model = Deposit
        fields = ['capacity', 'wilaya', 'baladiya', 'latitude', 'longitude']

    # You can define custom validation or additional behavior for the form if needed
    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic if needed
        return cleaned_data

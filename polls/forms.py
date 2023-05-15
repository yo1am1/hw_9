import phonenumbers
from django import forms
from django.core.exceptions import ValidationError

from .models import Number


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ["number"]

    def clean_number(self):
        phone_raw = self.cleaned_data["number"]
        try:
            phone = phonenumbers.parse(phone_raw, None)
        except phonenumbers.NumberParseException:
            raise ValidationError("Phone is invalid")
        if not phonenumbers.is_valid_number(phone):
            raise ValidationError("Phone is invalid")
        return phonenumbers.format_number(
            phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )

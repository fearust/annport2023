from django import forms
from agency.models import OnlineForm


class OnlineForm_Form(forms.ModelForm):
    class Meta:
        model = OnlineForm
        fields = ['name', 'phoneNumber', 'corp', 'email', 'customer_memo']
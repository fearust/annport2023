from django import forms
from academy.models import OnlineForm


class OnlineForm_Form(forms.ModelForm):
    class Meta:
        model = OnlineForm
        fields = ['name', 'phoneNumber', 'email', 'customer_memo']
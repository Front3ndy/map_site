from django import forms


class ContactFrom(forms.Form):
    name = forms.CharField(max_length=70)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=70)
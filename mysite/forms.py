from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
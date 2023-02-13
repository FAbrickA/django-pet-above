from django import forms
from education.models import Contact


class ContactFrom(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'maxlength': '128',
        # 'id': 'name',
        # 'name': 'name',
        'placeholder': '',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'maxlength': '128',
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'maxlength': '128',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '6',
        'maxlength': '1024',
    }))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')

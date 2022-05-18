from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):





    class Meta:
        model = Contact
        fields = ('name', 'email', 'text',)


    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})),
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'})),
    text = forms.Textarea(attrs={'class':'form-control'}),



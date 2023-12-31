from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Your Name'
        self.fields['email'].label = 'Your Email'
        self.fields['content'].label = 'Your Message'
        self.fields['content'].widget = forms.Textarea(attrs={'rows': 5})  # Adjust rows as needed

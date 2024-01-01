from django import forms
from .models import Contact
from user.models import CustomUser

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'content']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['name'].label = 'Your Name'
        self.fields['email'].label = 'Your Email'
        self.fields['content'].label = 'Your Message'
        self.fields['content'].widget = forms.Textarea(attrs={'rows': 5})  # Adjust rows as needed

        # If the user is authenticated, set labels to empty strings and hide the fields
        if user and user.is_authenticated:
            self.fields['name'].widget.attrs['readonly'] = True
            self.fields['name'].required = False
            self.fields['name'].widget.attrs['style'] = 'display:none;'
            self.fields['name'].initial = user.username
            self.fields['name'].label = ''

            self.fields['email'].widget.attrs['readonly'] = True
            self.fields['email'].required = False
            self.fields['email'].widget.attrs['style'] = 'display:none;'
            self.fields['email'].initial = user.email
            self.fields['email'].label = ''

            # Remove the 'image' field from the form
            self.fields.pop('image', None)

    # Add any additional validation or customization if needed

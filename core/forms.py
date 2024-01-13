from django import forms
from .models import Contact, Comment
from user.models import CustomUser


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['content', 'name', 'email']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['content'].label = 'Your Message'
        self.fields['content'].widget = forms.Textarea(attrs={'rows': 5})

        # Set initial values for name and email if the user is authenticated
        if self.user:
            self.fields['name'].initial = self.user.username
            self.fields['email'].initial = self.user.email

        # Remove the 'required' attribute for name and email fields
        self.fields['name'].required = False
        self.fields['email'].required = False

        # Add attributes for styling and making read-only if the user is authenticated
        if self.user:
            self.fields['name'].widget.attrs['readonly'] = True
            self.fields['name'].widget.attrs['style'] = 'color: black; background-color: #ACACAC; border: 1px solid #555;'
            self.fields['email'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['style'] = 'color: black; background-color: #ACACAC; border: 1px solid #555;'

    def save(self, commit=True):
        contact = super().save(commit=False)
        contact.user = self.user

        # Set email and name fields based on user info
        if self.user:
            contact.name = self.user.username
            contact.email = self.user.email

        if commit:
            contact.save()
        return contact

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }

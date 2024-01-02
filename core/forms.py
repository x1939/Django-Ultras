from django import forms
from .models import *
from user.models import CustomUser


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['content']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['content'].label = 'Your Message'
        self.fields['content'].widget = forms.Textarea(attrs={'rows': 5})

    def save(self, commit=True):
        contact = super().save(commit=False)
        contact.user = self.user

        # Set email and name fields based on user info
        if self.user:
            contact.name = self.user.username
            contact.email = self.user.email
        else:
            # If not logged in, set name and email to None
            contact.name = None
            contact.email = None

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
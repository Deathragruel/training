from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    """ A form for creating new blogs. """
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}

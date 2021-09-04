from .models import Post
from django.forms import ModelForm, TextInput, Textarea, ImageField


class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'description']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post Title'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
        }
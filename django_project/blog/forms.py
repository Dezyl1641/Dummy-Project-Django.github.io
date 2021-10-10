from django.db.models import fields
from django.forms import ModelForm
from django.forms import Textarea
from blog.models import Post
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields= ["company", "position", "content"]
        widgets = {
            'company': Textarea(attrs={'cols':30, 'rows':1,'placeholder': 'Company', 'class':'form-input'}),
            'position': Textarea(attrs={'cols':30, 'rows':1,'placeholder': 'position', 'class':'form-input'}),
            'content': Textarea(attrs={'cols':30, 'rows':4,'placeholder': 'Job Description', 'class':'form-input'}),
        }
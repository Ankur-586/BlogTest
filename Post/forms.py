from dataclasses import field
from .models import Post
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content','author','status']
        labels = {'title':'Title','author':'Author','status':'Status','content':'Content'}

        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'content':forms.Textarea(attrs={'class':'form-control'}),
        'author':forms.Select(attrs={'class':'form-control'},choices='Author'),
        'status':forms.Select(attrs={'class':'form-control'},choices='Status'),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['title','content']

        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'content':forms.Textarea(attrs={'class':'form-control'}),
        }
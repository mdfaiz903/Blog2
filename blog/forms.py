from django import forms
from . models import Post,Category
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'img', )
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'img', )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
    


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )
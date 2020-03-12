# from django import forms
from ckeditor_uploader.fields import RichTextUploadingField

from Posts.models import Post
from ckeditor_uploader.forms import forms


class PostForm(forms.ModelForm):
    body = RichTextUploadingField()

    class Meta:
        model = Post
        fields = ('title', 'body')
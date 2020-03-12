from ckeditor_uploader.fields import RichTextUploadingField

from Comments.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    comments = RichTextUploadingField()

    class Meta:
        model = Comment
        fields = ['comments']

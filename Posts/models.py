from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(verbose_name='Query Title', max_length=180)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField(verbose_name='Query Description', config_name='custom')

    def __str__(self):
        return "%s (%s)" % (self.title, self.user.first_name)

    def get_absolute_url(self):
        return reverse("post_detail", args=str(self.id))

    # def get_posts_as_markdown(self):
    #     return mark_safe(markdown(self.body, safe_mode='escape'))
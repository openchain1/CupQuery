from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from Posts.models import Post
from django.utils import timezone
# from markdown import markdown
# from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='posts', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = RichTextUploadingField(verbose_name='Leave a Comment :', null=True, config_name='custom')
    created_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField()
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.comments

    @property
    def total_likes(self):
        """
        Likes for the company
        :return: Integer: Likes for the company
        """
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.comments)
        super(Comment, self).save(*args, **kwargs)
from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

from alamnet.settings import AUTH_USER_MODEL
from src.comments.models import AbstractComment

class Post(models.Model):
    """ Post model """
    text = models.TextField(max_length=1024)
    create_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name='Post`s author', on_delete=models.CASCADE)

    def __str__(self):
        return f'Post {self.id} by {self.user}'

class Comment(AbstractComment, MPTTModel):
    """ Model for comment to post """
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name='Comment`s Author', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='Comment to post', related_name='comments', on_delete=models.CASCADE)
    parent = TreeForeignKey(
        'self',
        verbose_name='Parent comment',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return f'{self.user} {self.post}'
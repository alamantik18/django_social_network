from django.db import models

class AbstractComment(models.Model):
    """ Abstract comment model """
    text = models.TextField(verbose_name='Message', max_length=512)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
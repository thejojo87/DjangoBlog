from datetime import datetime

from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class BookInfo(models.Model):
    """
    博客文章
    """
    name = models.CharField(max_length=100, verbose_name="文集名")

    class Meta:
        verbose_name = '博客文集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


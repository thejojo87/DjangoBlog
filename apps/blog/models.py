from datetime import datetime

from django.db import models

from book.models import BookInfo
from DjangoUeditor.models import UEditorField
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class BlogInfo(models.Model):
    """
    博客文章
    """
    book = models.ForeignKey(BookInfo, verbose_name="所属文集")
    user = models.ForeignKey(User, verbose_name=u"用户")
    title = models.CharField(max_length=100, verbose_name="文章名")
    click_num = models.IntegerField(default=0, verbose_name="阅读数")
    blog_brief = models.TextField(max_length=500, verbose_name="文章简短描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    blog_main = UEditorField(verbose_name=u"内容", imagePath="blogs/images/", width=1000, height=300,
                              filePath="blogs/files/", default='')
    # 这里留着一个bool，可能加个密码什么的
    # ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")


    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

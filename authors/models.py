from django.conf import settings
from django.db import models

class Sects(models.Model):
    """派閥のモデル"""

    name = models.CharField(verbose_name='派',max_length=50)

    class Meta:
        db_table = 'sects'

    def __str__(self):
        return self.name

class Countries(models.Model):
    """国名のモデル"""

    name = models.CharField(verbose_name='国名',max_length=20,unique=True)

    class Meta:
        db_table = 'countries'

    def __str__(self):
        return self.name


class Authors(models.Model):
    """作者のモデル"""

    name = models.CharField(verbose_name='作者',max_length=50,unique=True)
    age = models.IntegerField(verbose_name='享年')
    country = models.CharField(verbose_name='国名',max_length=20)
    sect = models.ManyToManyField(Sects)
    fly_level = models.IntegerField(verbose_name='ヤバイ度',blank=True)

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.name


class Works(models.Model):
    """作品のモデル"""

    title = models.CharField(verbose_name='作品名',max_length=50)
    author = models.ForeignKey(Authors,on_delete=models.CASCADE)
    sect = models.ForeignKey(Sects,on_delete=models.PROTECT)

    class Meta:
        db_table = 'works'

    def __str__(self):
        return self.title


class Comments(models.Model):
    """
    コメント モデル
    works に対するコメント。
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    work = models.ForeignKey(Works, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='コメント本文')

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.body[:10]  # コメント本文の先頭10文字文だけを出力
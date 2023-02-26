from django.db import models

class Sects(models.Model):
    """派閥のモデル"""

    name = models.CharField(verbose_name='派',max_length=50,unique=True)

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
    countries = models.ManyToManyField(Countries)
    sects = models.ManyToManyField(Sects)
    fly_level = models.IntegerField(verbose_name='ヤバイ度',blank=True)

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.name


class Works(models.Model):
    """作品のモデル"""

    title = models.CharField(verbose_name='作品名',max_length=50)
    authors = models.ManyToManyField(Authors)

    class Meta:
        db_table = 'works'

    def __str__(self):
        return self.title


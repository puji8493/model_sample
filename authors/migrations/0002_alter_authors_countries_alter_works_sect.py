# Generated by Django 4.1.3 on 2023-02-26 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='countries',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authors.countries'),
        ),
        migrations.AlterField(
            model_name='works',
            name='sect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authors.sects'),
        ),
    ]

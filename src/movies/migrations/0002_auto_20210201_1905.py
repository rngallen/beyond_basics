# Generated by Django 3.1.5 on 2021-02-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercial',
            name='title',
            field=models.CharField(max_length=60, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='film',
            name='length',
            field=models.CharField(max_length=20, verbose_name='length'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=60, verbose_name='title'),
        ),
    ]
# Generated by Django 3.0.6 on 2020-08-11 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200810_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='info',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]

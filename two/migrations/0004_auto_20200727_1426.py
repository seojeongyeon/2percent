# Generated by Django 2.2.7 on 2020-07-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two', '0003_auto_20200727_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoshop',
            name='photobefore',
            field=models.ImageField(upload_to='image'),
        ),
    ]

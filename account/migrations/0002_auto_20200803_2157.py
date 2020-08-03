# Generated by Django 3.0.8 on 2020-08-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('two', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mscraps',
            field=models.ManyToManyField(related_name='mscrap_users', to='two.Mission'),
        ),
        migrations.AddField(
            model_name='user',
            name='pscraps',
            field=models.ManyToManyField(related_name='pscrap_users', to='two.Photoshop'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]

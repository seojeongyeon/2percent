# Generated by Django 3.1 on 2020-08-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('two', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
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
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email',)},
        ),
    ]

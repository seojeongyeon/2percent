<<<<<<< HEAD:account/migrations/0002_auto_20200808_1608.py
# Generated by Django 3.0.8 on 2020-08-08 16:08
=======
# Generated by Django 3.1 on 2020-08-08 14:17
>>>>>>> 9ed00c5e3a9e4d22640e3592c490f7c5259d9930:account/migrations/0002_auto_20200808_1417.py

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0001_initial'),
        ('two', '0001_initial'),
<<<<<<< HEAD:account/migrations/0002_auto_20200808_1608.py
        ('auth', '0011_update_proxy_permissions'),
=======
>>>>>>> 9ed00c5e3a9e4d22640e3592c490f7c5259d9930:account/migrations/0002_auto_20200808_1417.py
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
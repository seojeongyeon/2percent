# Generated by Django 3.0.8 on 2020-08-08 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='image')),
                ('point', models.IntegerField(default=0)),
                ('end_date', models.DateTimeField()),
                ('pick', models.IntegerField(blank=True, default=None, null=True)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mission', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photoshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('device', models.CharField(choices=[('핸드폰', 'phone'), ('카메라', 'camera'), ('필름카메라', 'filmcamera')], max_length=7)),
                ('color', models.CharField(choices=[('비비드한', 'vivid'), ('모노톤', 'mono'), ('빈티지한', 'Vintage')], max_length=8)),
                ('kind', models.CharField(choices=[('셀카', 'selfic'), ('풍경', 'scenery'), ('음식', 'food'), ('코디', 'style')], max_length=7)),
                ('method', models.CharField(choices=[('어플', 'apps'), ('기본카메라', 'basic')], max_length=8)),
                ('fix', models.CharField(choices=[('얼굴', 'face'), ('색감', 'color')], max_length=8)),
                ('app', models.CharField(max_length=10)),
                ('photobefore', models.ImageField(upload_to='image/')),
                ('photoafter', models.ImageField(upload_to='image/')),
                ('explain', models.TextField(help_text='사진에 적용된 보정법들을 모두 써주세요!')),
                ('photo_like', models.ManyToManyField(related_name='photo_like', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photoshop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MissionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='image')),
                ('isPicked', models.BooleanField(default=False)),
                ('likers', models.ManyToManyField(related_name='missionlikers', to=settings.AUTH_USER_MODEL)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='two.Mission')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='missionwriter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='contest_image_path')),
                ('contest_like', models.ManyToManyField(related_name='contest_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL)),
                ('photoshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='two.Photoshop')),
            ],
        ),
    ]

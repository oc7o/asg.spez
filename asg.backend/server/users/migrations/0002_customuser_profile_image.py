# Generated by Django 4.0.4 on 2022-05-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(default=1, upload_to=None, verbose_name='Users Profile Image'),
            preserve_default=False,
        ),
    ]

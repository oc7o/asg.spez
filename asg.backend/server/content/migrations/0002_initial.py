# Generated by Django 4.0.4 on 2022-05-08 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Page author'),
        ),
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='content.category', verbose_name='Site category'),
        ),
        migrations.AddField(
            model_name='page',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, related_name='pages', to='content.image', verbose_name='Pages images'),
        ),
        migrations.AddField(
            model_name='image',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sites.site', verbose_name='Page site'),
        ),
        migrations.AddField(
            model_name='document',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='sites.site', verbose_name='Page site'),
        ),
        migrations.AddField(
            model_name='category',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='Category site'),
        ),
    ]

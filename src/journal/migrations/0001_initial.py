# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 22:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('abstract', models.TextField(null=True)),
                ('date_submitted', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_published', models.DateTimeField(null=True)),
                ('open_for_comments', models.BooleanField(default=True)),
                ('doi', models.CharField(max_length=255, null=True)),
                ('authors', models.ManyToManyField(related_name='authors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of this journal', max_length=30)),
                ('logo', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.TextField()),
                ('number', models.PositiveIntegerField(default=0)),
                ('draft', models.BooleanField(default=True)),
                ('date_published', models.DateTimeField(null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Article')),
            ],
            options={
                'ordering': ('number',),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.License'),
        ),
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
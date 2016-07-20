# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.IntegerField(default=0)),
                ('upvotes_junior', models.IntegerField(default=0)),
                ('upvotes_senior', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=500)),
                ('option_a', models.CharField(max_length=50)),
                ('option_b', models.CharField(max_length=50)),
                ('option_c', models.CharField(max_length=50)),
                ('option_d', models.CharField(max_length=50)),
                ('correct_option', models.CharField(max_length=1)),
                ('upvotes_junior', models.IntegerField(default=0)),
                ('upvotes_senior', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

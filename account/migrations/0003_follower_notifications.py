# Generated by Django 3.1 on 2020-08-19 22:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20200820_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.URLField(blank=True, default=None, null=True)),
                ('time_created', models.DateTimeField(default=datetime.datetime(2020, 8, 20, 3, 45, 21, 439831))),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_date', models.DateTimeField(default=datetime.datetime(2020, 8, 20, 3, 45, 21, 439831))),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_set', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
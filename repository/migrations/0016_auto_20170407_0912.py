# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 01:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0015_auto_20170217_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trouble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('detail', models.TextField()),
                ('ctime', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(1, '未处理'), (2, '处理中'), (3, '已处理')], default=1)),
                ('solution', models.TextField(null=True)),
                ('ptime', models.DateTimeField(null=True)),
                ('pj', models.IntegerField(choices=[(1, '不满意'), (2, '一般'), (3, '活很好')], default=2, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='fans',
            field=models.ManyToManyField(related_name='f', through='repository.UserFans', to='repository.UserInfo', verbose_name='粉丝们'),
        ),
        migrations.AddField(
            model_name='trouble',
            name='processer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p', to='repository.UserInfo'),
        ),
        migrations.AddField(
            model_name='trouble',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u', to='repository.UserInfo'),
        ),
    ]

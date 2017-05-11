# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-10 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=40, unique=True)),
                ('device', models.ManyToManyField(to='one.Device')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True)),
                ('device', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='one.Device')),
            ],
        ),
        migrations.CreateModel(
            name='IpPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='IpRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='IpUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=50)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='one.IpUser')),
            ],
        ),
        migrations.AddField(
            model_name='iprole',
            name='user',
            field=models.ManyToManyField(blank=True, to='one.IpUser'),
        ),
        migrations.AddField(
            model_name='ippermission',
            name='roleperm',
            field=models.ManyToManyField(to='one.IpRole'),
        ),
        migrations.AddField(
            model_name='devicegroup',
            name='user',
            field=models.ManyToManyField(to='one.IpUser'),
        ),
    ]

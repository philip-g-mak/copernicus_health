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
            name='Medication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rx_name', models.CharField(max_length=180)),
                ('formulation', models.CharField(default=b'tab', max_length=180, choices=[(b'tab', b'Tablets'), (b'cap', b'Capsules'), (b'inj', b'Injections')])),
                ('total_quantity', models.IntegerField()),
                ('take_quantity', models.IntegerField()),
                ('prn', models.BooleanField(default=False)),
                ('freq', models.CharField(default=b'd', max_length=180, choices=[(b'd', b'Daily'), (b'w', b'Weekly')])),
                ('owner', models.ForeignKey(related_name='medications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('rx_name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=180)),
                ('last_name', models.CharField(max_length=180)),
                ('address1', models.CharField(max_length=180)),
                ('address2', models.CharField(max_length=180)),
                ('city', models.CharField(max_length=180)),
                ('state', models.CharField(max_length=180)),
                ('zip', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

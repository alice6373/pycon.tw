# Generated by Django 3.0.7 on 2020-08-23 15:28

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0017_merge_20200225_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='open role name')),
                ('description', models.TextField(verbose_name='open role descsription')),
                ('description_zh_hant', models.TextField(null=True, verbose_name='open role descsription')),
                ('description_en_us', models.TextField(null=True, verbose_name='open role descsription')),
                ('url', models.URLField(blank=True, max_length=255, verbose_name='open role URL')),
                ('sponsor', core.models.BigForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sponsors.Sponsor', verbose_name='sponsor')),
            ],
            options={
                'verbose_name': 'open role',
                'verbose_name_plural': 'open Roles',
            },
        ),
    ]

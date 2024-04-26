# Generated by Django 5.0.3 on 2024-04-05 20:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_name', models.CharField(max_length=70)),
                ('obj_address', models.CharField(max_length=200)),
                ('obj_coord', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('obj_description', models.TextField()),
            ],
            options={
                'verbose_name': 'Достопримечательность',
                'verbose_name_plural': 'Достопримечательности',
            },
        ),
    ]
# Generated by Django 5.0.3 on 2024-06-17 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0008_alter_objectsdata_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectsdata',
            name='url',
        ),
    ]
# Generated by Django 5.0.3 on 2024-06-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0006_objectsdata_image_alter_objectsdata_obj_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectsdata',
            name='url',
            field=models.SlugField(default='object', max_length=130, unique=True),
        ),
    ]

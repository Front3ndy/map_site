# Generated by Django 5.0.3 on 2024-04-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0005_objectsdata_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectsdata',
            name='image',
            field=models.ImageField(default=None, upload_to='object_images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='objectsdata',
            name='obj_address',
            field=models.CharField(max_length=200, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='objectsdata',
            name='obj_description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='objectsdata',
            name='obj_name',
            field=models.CharField(max_length=70, verbose_name='Название'),
        ),
    ]

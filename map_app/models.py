from django.contrib.postgres.fields import ArrayField
from django.db import models

STATUS_CHOISES = {
    'p': 'Published',
    'd': 'Draft',
}

class Category(models.Model):
    """ Описание модели категории """

    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class ObjectsData(models.Model):
    """ Описание модели достопримечательностей """

    obj_name = models.CharField(verbose_name='Название', max_length=70)
    obj_address = models.CharField(verbose_name='Адрес', max_length=200)
    obj_coord = ArrayField(models.FloatField())
    obj_description = models.TextField(verbose_name='Описание')
    obj_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOISES, default='d')
    image = models.ImageField(verbose_name='Изображение', upload_to='object_images/', default=None)

    def __str__(self):
        return self.obj_name

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'

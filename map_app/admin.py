from django.contrib import admin
from .models import Category, ObjectsData


@admin.action(description="Mark selected stories as published")
def make_published(modeladmin, request, queryset):
    queryset.update(status="p")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(ObjectsData)
class ObjectsDataAdmin(admin.ModelAdmin):
    list_display = ['obj_name', 'obj_category']
    ordering = ['obj_name', 'obj_category']
    actions = [make_published]


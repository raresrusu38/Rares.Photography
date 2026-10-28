from django.contrib import admin

# Register your models here.

from .models import Category, Photo

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'uploaded_at')
    list_filter = ('category',)

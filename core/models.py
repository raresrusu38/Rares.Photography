# Create your models here.
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nume Categorie")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categorii"

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Titlu Foto")
    image = models.ImageField(upload_to='portfolio/', verbose_name="Fișier Imagine")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='photos', verbose_name="Categorie")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Fotografii"
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title or f"Foto #{self.id}"

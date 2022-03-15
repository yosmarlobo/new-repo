from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=250, )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250, )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.name

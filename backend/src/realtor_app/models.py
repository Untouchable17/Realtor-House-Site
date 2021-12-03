from django.db import models
from datetime import datetime


class Realtor(models.Model):

    name = models.CharField(max_length=70, verbose_name="Имя риэлтора")
    email = models.EmailField(unique=True, max_length=255)
    image = models.ImageField(upload_to="realtors/", verbose_name="Фото риэлтора")
    description = models.TextField(max_length=5000, blank=True, verbose_name="Биография/Описание")
    rating_top = models.BooleanField(default=False, verbose_name="Лучший риэлтор?")
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.name} | {self.email}"



from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from src.realtor_app.models import Realtor


"""
    Категория дома (Дом/Квартира/Таунхаус)
    Тип дома (Продажа/Аренда)
    
    Поля:
    -- Адрес дома (или номер)
    -- Ссылка (slug)
    -- Почтовый индекс дома
    -- Город/Улица (CharField)
    -- Цена дома 
    -- Описание дома
    -- Лицевое изображение дома
    -- Дополнительные фотографии дома
    -- Количество ванных комнат (intField)
    -- Количество спальных комнат 
    -- Количество просмотров дома
    -- Количество кв.метров
    -- Есть ли предосмотр дома? (Boolean)
    -- Дата публикации объявления (datetime)
"""


class SaleTypeCategory(models.Model):

    title = models.CharField(max_length=255, verbose_name="Тип продажи")
    slug = models.SlugField(unique=True, verbose_name="Ссылка на категорию")

    def __str__(self):
        return self.title


class HomeTypeCategory(models.Model):

    title = models.CharField(max_length=255, verbose_name="Тип дома")
    slug = models.SlugField(unique=True, verbose_name="Ссылка на категорию")

    def __str__(self):
        return self.title


class House(models.Model):

    title = models.CharField(max_length=255, verbose_name="название/номер")
    slug = models.SlugField(unique=True, verbose_name="Ссылка на дом")
    main_picture = models.ImageField(upload_to="houses/%Y/%m/%d/", verbose_name="Изображение дома")

    description = models.TextField(verbose_name="Описание дома")
    # address = models.CharField(max_length=255, verbose_name="Адрес дома")
    # city = models.CharField(max_length=255, verbose_name="Город")
    # zipcode = models.CharField(max_length=255, verbose_name="Почтовый индекс")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена дома")
    bedrooms = models.IntegerField(verbose_name="Количество спальных комнат")
    house_views = models.IntegerField(default=0, verbose_name="Количество просмотров")
    bathrooms = models.IntegerField(verbose_name="Количество ванных комнат")
    sale_type = models.ForeignKey(SaleTypeCategory, related_name="sale_type", on_delete=models.DO_NOTHING)
    home_type = models.ForeignKey(HomeTypeCategory, related_name="home_type", on_delete=models.DO_NOTHING)
    sqft = models.IntegerField(verbose_name="количество кв.метров")
    open_house = models.BooleanField(default=False, verbose_name="Доступен для предосмотра?")
    is_published = models.BooleanField(default=True, verbose_name="Доступен данный дом?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    realtors = models.ManyToManyField(Realtor, related_name="chose_realtor", verbose_name="Выбрать риэлтора", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('house-detail', kwargs={"slug": self.slug})


class HomeImages(models.Model):

    image = models.ImageField("Изображение", upload_to="movie_shots/")
    house = models.ForeignKey(House, verbose_name="Домик", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return str(self.image)
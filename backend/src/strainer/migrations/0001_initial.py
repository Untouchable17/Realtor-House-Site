# Generated by Django 3.2.9 on 2021-12-03 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeTypeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тип дома')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка на категорию')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название/номер')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка на дом')),
                ('main_picture', models.ImageField(upload_to='houses/%Y/%m/%d/', verbose_name='Изображение дома')),
                ('description', models.TextField(verbose_name='Описание дома')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес дома')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('zipcode', models.CharField(max_length=255, verbose_name='Почтовый индекс')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена дома')),
                ('bedrooms', models.IntegerField(verbose_name='Количество спальных комнат')),
                ('house_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('bathrooms', models.IntegerField(verbose_name='Количество ванных комнат')),
                ('sqft', models.IntegerField(verbose_name='количество кв.метров')),
                ('open_house', models.BooleanField(default=False, verbose_name='Доступен для предосмотра?')),
                ('is_published', models.BooleanField(default=True, verbose_name='Доступен данный дом?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('home_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='home_type', to='strainer.hometypecategory')),
            ],
        ),
        migrations.CreateModel(
            name='SaleTypeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тип продажи')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка на категорию')),
            ],
        ),
        migrations.CreateModel(
            name='StrainerHomeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Изображение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strainer.house', verbose_name='Домик')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.AddField(
            model_name='house',
            name='sale_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sale_type', to='strainer.saletypecategory'),
        ),
    ]

from django.db import models

class Recipes(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название рецепта')
    content = models.TextField(blank=True, verbose_name='Содержание рецепта')
    dt_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    dt_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотографии')
    is_publ = models.BooleanField(default=True, verbose_name='Публикация')
    time = models.CharField(blank=True, max_length=50, verbose_name='Время приготовления')
    energy_value = models.TextField(blank=True, verbose_name='Энергетичекская ценность')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse_lazy
        return reverse_lazy('recipe', kwargs={'rec_id': self.pk})

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class Category(models.Model):
    name = models.CharField(max_length=155, verbose_name='Название категории')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse_lazy
        return reverse_lazy('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
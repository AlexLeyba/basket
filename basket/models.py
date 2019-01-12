from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from time import time
from django.urls import reverse
from .utils import transliteration_rus_eng


class Category(MPTTModel):
    """Модель категорий"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Название категории", max_length=100)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=150, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    class MPTTMeta:
        order_insertion_by = ['name']


class ProductList(models.Model):
    """Список покупок"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField("Товар", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True)
    date = models.DateTimeField("дата добавления", auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'список товаров'
        verbose_name_plural = 'списки товаров'

    def __str__(self):
        return "{}".format(self.user)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.item)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_list')


def gen_slug(s):
    """автоматическая генерация slug"""
    new_slug = slugify(transliteration_rus_eng(s), allow_unicode=True)
    return new_slug + '-' + str(int(time()))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Category.objects.create(user=instance, id=instance.id, name='Продукты', slug='product')

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from api.helper import get_webp_image, get_thumb_image

class UserProfile(models.Model):
    ROLES = (
        (1, 'admin'),
        (2, 'manager'),
        (3, 'customer')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(verbose_name="Роль", choices=ROLES, default=3)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Menu(models.Model):
    name = models.CharField(verbose_name="Название", unique=True, max_length=64)

    def __str__(self):
        return self.name

class SubMenu(models.Model):
    name = models.CharField(verbose_name="Название", unique=True, max_length=64)
    menu_item = models.ForeignKey(Menu, related_name="sub_menu", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(verbose_name="Название", unique=True, max_length=64)
    url_alias = models.CharField(verbose_name="Url адрес", unique=True, max_length=64)
    meta_keywords = models.TextField(verbose_name="meta keywords", max_length=255)
    meta_description = models.TextField(verbose_name="meta description", max_length=255)
    image = models.ImageField(verbose_name="Изображение", upload_to="./category")
    compressed_image = models.ImageField(verbose_name="Изображение", upload_to="./category", blank=True)
    sub_menu_item = models.ForeignKey(SubMenu, related_name="category", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.image:
            self.image = get_thumb_image(self.image, 500)
            self.compressed_image = get_webp_image(self.image)
            super(Category, self).save()

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(verbose_name="Название", max_length=64)
    long_description = models.TextField(verbose_name="Описание", max_length=1000)
    short_description = models.TextField(verbose_name="Сниппет", max_length=255)
    meta_keywords = models.TextField(verbose_name="meta keywords", max_length=255)
    meta_description = models.TextField(verbose_name="meta description", max_length=255)
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=7)
    discount = models.DecimalField(verbose_name="Скидка", decimal_places=2, max_digits=7)
    category = models.ManyToManyField(Category, related_name="products", through='ProductCategory')

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Image(models.Model):
    alt = models.CharField(verbose_name="Alt", max_length=32, default='')
    origin_inner = models.ImageField(verbose_name="Изображение", upload_to="./catalog/inner")
    origin_thumb = models.ImageField(verbose_name="Маленькое изображение", upload_to="./catalog/thumb", blank=True)
    compressed_inner = models.ImageField(verbose_name="Сжатое изображение", upload_to="./catalog/inner", blank=True)
    compressed_thumb = models.ImageField(verbose_name="Сжатое изображение тизер", upload_to="./catalog/thumb", blank=True)
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    color = models.ForeignKey('Option', on_delete=models.DO_NOTHING, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.origin_inner:
            self.origin_thumb = get_thumb_image(self.origin_inner, 300)
            self.compressed_inner = get_webp_image(self.origin_inner)
            self.compressed_thumb = get_webp_image(self.origin_thumb)
            super(Image, self).save()


class OptionGroup(models.Model):
    name = models.CharField(verbose_name="Название", max_length=16, unique=True)
    machine_name = models.CharField(verbose_name="Машинное имя", max_length=32, unique=True)

    def __str__(self):
        return self.name

class Option(models.Model):
    name = models.CharField(verbose_name="Название", max_length=32)
    value = models.CharField(verbose_name="Значение", max_length=32)
    group = models.ForeignKey(OptionGroup, related_name="options", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="options", through="ProductOptions")

    def __str__(self):
        return self.name

class ProductOptions(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

class Block(models.Model):
    name = models.CharField(verbose_name="Название", max_length=32, unique=True)
    weight = models.IntegerField(verbose_name="Вес", default=0)

    def __str__(self):
        return self.name

class SliderBlock(models.Model):
    type = models.CharField(verbose_name="Тип", max_length=20, default="slider")
    title = models.CharField(verbose_name="Заголовок", max_length=32)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="slider")
    products = models.ManyToManyField(Product, through='SliderProduct')

    def __str__(self):
        return self.title

class SliderProduct(models.Model):
    slider = models.ForeignKey(SliderBlock, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class BannerBlock(models.Model):
    ALIGN_HORISONTAL = (
        (1, 'left'),
        (2, 'center'),
        (3, 'right')
    )
    ALIGN_VERTICAL = (
        (1, 'top'),
        (2, 'center'),
        (3, 'bottom')
    )
    type = models.CharField(verbose_name="Тип", max_length=20, default="banner")
    link = models.CharField(verbose_name="Ссылка", max_length=255)
    button_text = models.CharField(verbose_name="Текст кнопки", max_length=255)
    text_size = models.IntegerField(verbose_name="Размер текста", default=40, validators=[MaxValueValidator(50), MinValueValidator(30)])
    text = models.CharField(verbose_name="Текст", max_length=255)
    align_text_horisontal = models.IntegerField(verbose_name="Выравнивание текста по горизонтали", choices=ALIGN_HORISONTAL)
    align_text_vertical = models.IntegerField(verbose_name="Выравнивание текста по вертикали", choices=ALIGN_VERTICAL)
    align_button_horisontal = models.IntegerField(verbose_name="Выравнивание кнопки по горизонтали", choices=ALIGN_HORISONTAL)
    align_button_vertical = models.IntegerField(verbose_name="Выравнивание кнопки по вертикали", choices=ALIGN_VERTICAL)
    image = models.ImageField(verbose_name="Изображение", upload_to="./banner")
    compressed_image = models.ImageField(verbose_name="Изображение", upload_to="./banner", blank=True)
    is_full = models.BooleanField(verbose_name="На весь экран", default=False)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="banner")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.image:
            self.compressed_image = get_webp_image(self.image)
            super(BannerBlock, self).save()

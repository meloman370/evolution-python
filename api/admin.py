from django.contrib import admin
from .models import Menu, SubMenu, Category
from .models import Product, Image, OptionGroup
from .models import Option, ProductOptions, CategoryOptionGroup

# Register your models here.
admin.site.register(Menu)
admin.site.register(SubMenu)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(OptionGroup)
admin.site.register(Option)
admin.site.register(ProductOptions)
admin.site.register(CategoryOptionGroup)

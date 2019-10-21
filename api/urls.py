from django.urls import path
from api.views.menu import MenuCreateView, MenuView, MenuListView, MenuUpdateView
from api.views.sub_menu import SubMenuCreateView, SubMenuView, SubMenuListView, SubMenuUpdateView
from api.views.category import CategoryCreateView, CategoryView, CategoryListView, CategoryEditView
from api.views.product import ProductCreateView, ProductView, ProductListView, ProductUpdateView
from api.views.image import ImageCreateView, ImageView, ImageListView, ImageUpdateView
from api.views.option_group import OptionGroupCreateView, OptionGroupView, OptionGroupListView
from api.views.option import OptionCreateView, OptionView, OptionListView, ProductOptionsCreateView, ProductOptionDeleteByProduct
from api.views.slider_block import SliderBlockCreateView, SliderBlockListView, SliderBlockView, SliderBlockUpdateView
from api.views.slider_block import SliderProductListView, SliderProductView, SliderProductCreateView, SliderProductDeleteProducts
from api.views.block import BlockCreateView, BlockListView, BlockView, BlockUpdateView
from api.views.banner_block import BannerBlockCreateView, BannerBlockListView, BannerBlockView, BannerBlockUpdateView
from api.views.product_category import ProductCategoryCreateView, ProductCategoryView, ProductCategoryListView, ProductCategoryDeleteByProduct
from api.views.user_profile import UserProfileView

urlpatterns = [
    path('menu/create', MenuCreateView.as_view()),
    path('menu/<int:pk>/edit', MenuUpdateView.as_view()),
    path('menu/<int:pk>', MenuView.as_view()),
    path('menu/', MenuListView.as_view()),

    path('sub-menu/create', SubMenuCreateView.as_view()),
    path('sub-menu/<int:pk>/edit', SubMenuUpdateView.as_view()),
    path('sub-menu/<int:pk>', SubMenuView.as_view()),
    path('sub-menu/', SubMenuListView.as_view()),

    path('category/create', CategoryCreateView.as_view()),
    path('category/<int:pk>/edit', CategoryEditView.as_view()),
    path('category/<int:pk>', CategoryView.as_view()),
    path('categories/', CategoryListView.as_view()),

    path('product/create', ProductCreateView.as_view()),
    path('product/<int:pk>', ProductView.as_view()),
    path('product/<int:pk>/edit', ProductUpdateView.as_view()),
    path('products/', ProductListView.as_view()),

    path('product/category/create', ProductCategoryCreateView.as_view()),
    path('product/category/<int:pk>', ProductCategoryView.as_view()),
    path('product/categories/', ProductCategoryListView.as_view()),
    path('product/<int:pk>/categories/delete', ProductCategoryDeleteByProduct.as_view()),

    path('product/image/create', ImageCreateView.as_view()),
    path('product/image/<int:pk>', ImageView.as_view()),
    path('product/image/<int:pk>/edit', ImageUpdateView.as_view()),
    path('product/images/', ImageListView.as_view()),

    path('option-group/create', OptionGroupCreateView.as_view()),
    path('option-group/<int:pk>', OptionGroupView.as_view()),
    path('option-groups/', OptionGroupListView.as_view()),

    path('widget/option/create', OptionCreateView.as_view()),
    path('widget/option/<int:pk>', OptionView.as_view()),
    path('widget/options/', OptionListView.as_view()),
    path('widget/product-option/create', ProductOptionsCreateView.as_view()),
    path('product/<int:pk>/options/delete', ProductOptionDeleteByProduct.as_view()),

    path('block/create', BlockCreateView.as_view()),
    path('block/<int:pk>/edit', BlockUpdateView.as_view()),
    path('blocks/', BlockListView.as_view()),
    path('block/<int:pk>', BlockView.as_view()),

    path('slider-block/create', SliderBlockCreateView.as_view()),
    path('slider-blocks/', SliderBlockListView.as_view()),
    path('slider-block/<int:pk>/edit', SliderBlockUpdateView.as_view()),
    path('slider-block/<int:pk>', SliderBlockView.as_view()),
    path('slider-block/<int:pk>/products/delete', SliderProductDeleteProducts.as_view()),

    path('slider-block/product/create', SliderProductCreateView.as_view()),
    path('slider-block/products/', SliderProductListView.as_view()),
    path('slider-block/product/<int:pk>', SliderProductView.as_view()),

    path('banner-block/create', BannerBlockCreateView.as_view()),
    path('banner-blocks/', BannerBlockListView.as_view()),
    path('banner-block/<int:pk>', BannerBlockView.as_view()),
    path('banner-block/<int:pk>/edit', BannerBlockUpdateView.as_view()),

    path('my-profile/', UserProfileView.as_view())
]

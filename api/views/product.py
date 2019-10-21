from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from api.serializers.product import ProductSerializer, ProductListSerializer
from api.serializers.product import ProductCreateSerializer
from api.models import Product

class ProductPagination(PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    max_page_size = 24

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer

class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()

class ProductView(generics.RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        queryset = Product.objects.order_by().distinct()
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        category = self.request.query_params.get('category', None)
        title = self.request.query_params.get('title', None)
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
        if category is not None:
            queryset = queryset.filter(category=category)
        if title is not None:
            queryset = queryset.filter(title__contains=title)
        return queryset

from rest_framework import generics
from api.serializers.category import CategorySerializer, CategoryCreateSerializer, CategoryListSerializer
from api.models import Category

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryCreateSerializer

class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        queryset = Category.objects.all()
        url_alias = self.request.query_params.get('url_alias', None)
        if url_alias is not None:
            queryset = queryset.filter(url_alias=url_alias)
        return queryset

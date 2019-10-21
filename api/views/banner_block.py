from rest_framework import generics
from api.serializers.banner_block import BannerBlockSerializer, BannerBlockCreateSerializer
from api.models import BannerBlock

class BannerBlockCreateView(generics.CreateAPIView):
    serializer_class = BannerBlockCreateSerializer

class BannerBlockUpdateView(generics.UpdateAPIView):
    serializer_class = BannerBlockCreateSerializer
    queryset = BannerBlock.objects.all()

class BannerBlockView(generics.RetrieveDestroyAPIView):
    serializer_class = BannerBlockSerializer
    queryset = BannerBlock.objects.all()

class BannerBlockListView(generics.ListAPIView):
    serializer_class = BannerBlockSerializer
    queryset = BannerBlock.objects.all()
